# flake8:noqa
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for
)

from werkzeug.security import (
    check_password_hash, generate_password_hash
)

from movedbymovies.db import get_db
from movedbymovies.util.password_validators import ValidatePassword
from movedbymovies.util.my_exceptions import (
    HasNoPunctuation, HasNotEnoughLength, HasNoUppercase, HasNoNumbers
)

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        email = request.form['email']
        birth = request.form['birth']

        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required.'
        elif password != confirm_password:
            error = "Password's dont match."
        
        try:
            ValidatePassword(password)
        except HasNoPunctuation as e:
            error = str(e)
        except HasNoNumbers as e:
            error = str(e)
        except HasNotEnoughLength as e:
            error = str(e)
        except HasNoUppercase as e:
            error = str(e)       

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password, email, birth) VALUES(?,?,?,?,)",
                    (username, generate_password_hash(password), email, birth),
                )
                db.commit()
            except db.IntegrityError:
                error = f'User email ({email} )is already registered.'
            else:
                return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
