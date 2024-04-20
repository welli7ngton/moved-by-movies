from flask import (
    Blueprint, flash, render_template, session, redirect, url_for, request
)

from movedbymovies.db import get_db


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

    movies = session.get('cart')
    movies.pop(request.form['removed-movie'])
    flash('Movie removed.')
    return redirect(url_for('cart.my_cart'))
