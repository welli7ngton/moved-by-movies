# flake8: noqa
from flask import (
    Blueprint, flash, render_template, request
)

from movedbymovies.db import get_db
from movedbymovies.auth import login_required


bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('/catalog', methods=('GET','POST'))
def catalog():
    db = get_db()
    
    movies = db.execute(
        '''SELECT id, poster, title, plot, runtime, released,
        gender, director, imdbRating 
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


@bp.route('/movie_detail/<int:_id>', methods=('GET',))
def movie_detail(_id: int):
    db = get_db()
    
    movie = db.execute(
        'SELECT * FROM movies WHERE id = ?',
        (_id,),
    ).fetchall()

    return render_template('movies/movie_detail.html', movie=movie)
