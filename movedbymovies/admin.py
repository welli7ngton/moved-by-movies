# flake8: noqa
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
import os
from dotenv import load_dotenv
import requests

import functools

from flask import (
    Blueprint, flash, redirect, g, render_template, request,
    session, url_for
)

from werkzeug.security import (
    check_password_hash
)

from movedbymovies.db import get_db
from movedbymovies.util.trigger import Trigger

load_dotenv()

API_KEY = os.getenv('API_KEY')
HOST = 'https://www.omdbapi.com/'

bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('admin.login'))
        return view(**kwargs)
    return wrapped_view


@bp.route('/', methods=('GET',))
@admin_required
def home():
    return render_template('admin/base.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM admin WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('admin.home'))

        flash(error)

    return render_template('admin/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.home'))


@bp.route('/register', methods=('GET', 'POST'))
@admin_required
def register_movie():
    if request.method == 'POST':
        title = request.form['movie-title']

        db = get_db()
        error = None

        if not title:
            error = 'Movie Title is required.'

        if error is None:
            response = requests.get(f'{HOST}?t={title}&apikey={API_KEY}&plot=full')
            querry = """INSERT INTO movies
                        (title, plot, released, runtime,
                        gender, director, poster, imdbRating,
                        actors, awards, writer, country,
                        language)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            title = response.json()

            try:
                Trigger.movie_registered(session.get('user_id'), db)
                db.execute(
                    querry,
                    (
                        title['Title'], title['Plot'], title['Released'],
                        title['Runtime'], title['Genre'], title['Director'],
                        title['Poster'], title['imdbRating'],
                        title['Actors'], title['Awards'],
                        title['Writer'], title['Country'],
                        title['Language']
                    ),
                )
                db.commit()
                flash(f'Movie ({title["Title"]}) Registered!')
            except KeyError:
                flash(f'Movie ({request.form["movie-title"]}) not Found :(')

    return render_template('admin/register_movie.html')


@bp.route('/users', methods=('GET', 'POST'))
def users():
    db = get_db()

    users = db.execute('SELECT * FROM users').fetchall()

    return render_template('admin/users.html', users=users)


@bp.route('/single_user/<int:_id>', methods=('GET', 'POST'))
def single_user(_id):
    db = get_db()

    user = db.execute('SELECT * FROM users WHERE id == ?', (_id,)).fetchall()

    if request.method == 'POST':
        try:
            _ = request.form['set-admin']
            db.execute(
                'UPDATE users SET is_admin = ? WHERE id = ?',
                (1, _id)
            )
            db.commit()
            flash('User updated!')
            return redirect(url_for('admin.users'))
        except KeyError:
            db.execute(
                'UPDATE users SET is_admin = ? WHERE id = ?',
                (0, _id)
            )
            db.commit()
            flash('User updated!')
            return redirect(url_for('admin.users'))

    return render_template('admin/single_user.html', user=user[0])


@bp.route('/delete_user/<int:_id>', methods=('GET', 'POST'))
def delete_user(_id):
    db = get_db()

    if request.method == 'POST':
        password = request.form['password']
        user = db.execute('SELECT * FROM admin WHERE id = ?', (session.get('user_id'),)).fetchone()

        if session and check_password_hash(user['password'], password):
            Trigger.delete(session.get('user_id'), request.form['motivation'], db)
            db.execute('DELETE FROM users WHERE id = ?', (_id,))
            db.commit()
            flash('User Deleted!')
            return redirect(url_for('admin.users'))
        flash('Incorrect Password')

    return render_template('admin/delete_user.html')
