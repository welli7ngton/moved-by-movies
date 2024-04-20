# flake8: noqa
from flask import (
    Blueprint, flash, render_template, request, redirect, url_for, g, session
)

from movedbymovies.db import get_db


bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('/catalog', methods=('GET', 'POST'))
def catalog():
    db = get_db()
    movies = db.execute(
        '''SELECT id, poster, title, plot, runtime, released,
        gender, director, imdbRating, price
        FROM movies'''
    ).fetchall()

    return render_template('movies/catalog.html', movies=movies)


@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['movie-title']
        director = request.form['director']
        year = request.form['year']

        db = get_db()
        error = None

        if not title and director == "" and year == "":
            error = 'At least Title is required to make the search.'

        if error is None:
            if title and director and year:
                movies = db.execute(
                    'SELECT * FROM movies WHERE title LIKE ? OR director LIKE ? OR released LIKE ?',
                    (f'%{title}%', f'%{director}%', f'%{year}'),
                ).fetchall()
            elif title and director and year == "":
                movies = db.execute(
                    'SELECT * FROM movies WHERE title LIKE ? OR director LIKE ?',
                    (f'%{title}%', f'%{director}%'),
                ).fetchall()
            elif title and year and director == "":
                movies = db.execute(
                    'SELECT * FROM movies WHERE title LIKE ? OR released LIKE ?',
                    (f'%{title}%', f'%{year}'),
                ).fetchall()
            elif director and year and title == "":
                movies = db.execute(
                    'SELECT * FROM movies WHERE director LIKE ? OR released LIKE ?',
                    (f'{director}', f'%{year}'),
                ).fetchall()
            elif director and title == "" and year == "":
                movies = db.execute(
                    'SELECT * FROM movies WHERE director LIKE ?',
                    (f'%{director}%',),
                ).fetchall()
            elif year and title == "" and director == "":
                movies = db.execute(
                    'SELECT * FROM movies WHERE released LIKE ?',
                    (f'%{year}',),
                ).fetchall()
            elif title and director == "" and year == "":
                movies = db.execute(
                    'SELECT * FROM movies WHERE title LIKE ?',
                    (f'%{title}%',),
                ).fetchall()

            return render_template('movies/search.html', movies=movies, total=len(movies))

        flash(error)
    return render_template('movies/search.html')


@bp.route('/movie_detail/<int:_id>', methods=('GET', 'POST'))
def movie_detail(_id: int):
    db = get_db()

    movie = db.execute(
        'SELECT * FROM movies WHERE id = ?',
        (_id,),
    ).fetchone()
    
    if request.method == 'POST' and g.user is not None:
        return redirect(url_for('cart.add_movie', movie_id=movie['id']))

    return render_template('movies/movie_detail.html', movie=movie)


@bp.route('/my_movies', methods=('GET',))
def my_movies():
    db = get_db()
    movies = db.execute(
        """SELECT * FROM movies
        INNER JOIN purchases ON purchases.movie_id = movies.id
        WHERE user_id = ?
        """,
        (session.get('user_id'),)
    ).fetchall()
    if movies:
        return render_template('movies/my_movies.html', movies=movies)
    return render_template('movies/my_movies.html', movies=False)
