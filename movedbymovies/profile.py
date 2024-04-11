from flask import (
    Blueprint, flash, redirect, render_template, request,
    session, url_for, jsonify
)

from movedbymovies.auth import login_required
from movedbymovies.db import get_db

from werkzeug.security import check_password_hash, generate_password_hash

from movedbymovies.util.password_validators import ValidatePassword
from movedbymovies.util.my_exceptions import (
    HasNoPunctuation, HasNotEnoughLength, HasNoUppercase, HasNoNumbers
)

bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/me', methods=('GET',))
@login_required
def profile():
    return render_template('profile/profile.html')


@bp.route('/changes', methods=('GET', 'POST'))
@login_required
def change_username_and_birth():
    if request.method == 'POST':
        new_username = request.form['username']
        new_birth = request.form['birth']
        password = request.form['password']

        db = get_db()
        error = None

        if not new_username:
            error = 'Username is required.'
        if not new_birth:
            error = 'Birth is required.'
        if not password:
            error = 'Password is required.'

        user = db.execute(
            'SELECT * FROM users WHERE id = ?',
            (session.get('user_id'),)
        ).fetchone()

        if not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            db.execute(
                'UPDATE users SET username = ?, birth = ? WHERE id = ?',
                (new_username, new_birth, session.get('user_id')),
            )
            db.commit()
            return redirect(url_for('profile.profile'))
        flash(error)
    return render_template('profile/change_profile.html')


@bp.route('/change-password', methods=('GET', 'POST'))
@login_required
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        error = None

        if not new_password:
            error = 'New password is required.'
        if not email:
            error = 'Email is required.'
        if not password:
            error = 'Password is required.'

        try:
            ValidatePassword(password)
        except HasNoPunctuation as e:
            return jsonify({'error': f'{str(e)}'})
        except HasNoNumbers as e:
            return jsonify({'error': f'{str(e)}'})
        except HasNotEnoughLength as e:
            return jsonify({'error': f'{str(e)}'})
        except HasNoUppercase as e:
            return jsonify({'error': f'{str(e)}'})

        user = db.execute(
            'SELECT * FROM users WHERE id = ?',
            (session.get('user_id'),)
        ).fetchone()

        if not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            db.execute(
                'UPDATE users SET password = ? WHERE id = ?',
                (generate_password_hash(new_password), session.get('user_id')),
            )
            db.commit()
            flash('Password changed.')
            return redirect(url_for('profile.profile'))
        flash(error)
    return render_template('profile/change_password.html')
