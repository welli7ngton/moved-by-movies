# flake8: noqa
from random import randint

from flask import (
    Blueprint, flash, render_template, session, redirect, url_for, request, g
)

from movedbymovies.db import get_db
from movedbymovies.auth import login_required

bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/add_movie/<int:movie_id>', methods=('GET',))
def add_movie(movie_id):
    db = get_db()
    movie = db.execute(
        'SELECT  title, id, poster, plot, price FROM movies WHERE id = ?',
        (movie_id,)
    ).fetchone()
    flash(f'Movie {movie["title"]} added to the cart!')
    try:
        session['cart'].update({movie[0]: [data for data in movie[1:]]})
    except KeyError:
        session['cart'] = {movie[0]: [data for data in movie[1:]]}

    return redirect(url_for('movies.catalog'))


@bp.route('/my_cart', methods=('GET', 'POST'))
def my_cart():
    if request.method == 'GET':
        movies = session.get('cart')
        if movies:
            price = sum([v[3] for m, v in movies.items()])
            return render_template('cart/my_cart.html', movies=movies, price=price)
        return render_template('cart/my_cart.html', movies=None, price=None)

    if 'removed-movie' in request.form:
        movies = session.get('cart')
        movies.pop(request.form['removed-movie'])
        flash(f'Movie ({request.form["removed-movie"]}) removed.')
        return redirect(url_for('cart.my_cart'))
    elif 'finish-purchase' in request.form:
        user_balance = float(g.user['balance'])
        user_balance -= float(request.form['price'])
        
        db = get_db()
        db.execute('UPDATE users SET balance = ? WHERE id = ?', (user_balance, session.get('user_id')))
        db.commit()
        _ids = request.form.getlist('_ids')
        for _ in _ids:
            db.execute('INSERT INTO purchases (user_id, movie_id) VALUES (?, ?)',
                    (session.get('user_id'), _))
        db.commit()
        session.pop('cart')
        flash('Purchase finished')
        return redirect(url_for('movies.my_movies'))


@bp.route('/buy_credits', methods=('GET','POST'))
@login_required
def buy_credits():
    db = get_db()
    
    if request.method == 'POST':
        db.execute('UPDATE users SET balance = ? WHERE id = ?', (randint(7,999), session.get('user_id'),))
        db.commit()
        flash('Credits added to your account, thank you for the support :>')
        return redirect(url_for('movies.catalog'))
    return render_template('cart/buy_credits.html')
