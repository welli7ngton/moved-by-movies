from flask import (
    Blueprint, flash, render_template, session, redirect, url_for
)

from movedbymovies.db import get_db


bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/add_movie/<int:movie_id>', methods=('GET',))
def add_movie(movie_id):
    db = get_db()
    movie = db.execute(
        'SELECT  title, poster, plot, price FROM movies WHERE id = ?',
        (movie_id,)
    ).fetchone()
    flash(f'Movie {movie["title"]} added to the cart!')
    try:
        session['cart'].update({movie[0]: [movie[1], movie[2], movie[3]]})
    except KeyError:
        session['cart'] = {movie[0]: [movie[1], movie[2], movie[3]]}

    return redirect(url_for('movies.catalog'))


@bp.route('/my_cart', methods=('GET', 'POST'))
def my_cart():
    movies = session.get('cart')
    if movies:
        price = sum([v[2] for m, v in movies.items()])
        return render_template('cart/my_cart.html', movies=movies, price=price)
    return render_template('cart/my_cart.html', movies=None, price=None)
