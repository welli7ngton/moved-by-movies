# flake8: noqa
import os
from dotenv import load_dotenv
import requests

from flask import (
    Blueprint, flash, render_template, request,
)

from movedbymovies.db import get_db
from movedbymovies.auth import login_required

load_dotenv()

bp = Blueprint('movies', __name__, url_prefix='/movies')

API_KEY = os.getenv('API_KEY')
HOST = 'https://www.omdbapi.com/'


@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    if request.method == 'POST':
        title = request.form['movie-title']

        db = get_db()
        error = None

        if not title:
            error = 'Movie Title is required.'


        if error is None:
            response = requests.get(f'{HOST}?t={title}&apikey={API_KEY}&plot=full')
            

            title = response.json()
            try:
                db.execute(
                    """INSERT INTO movies
                        (title, plot, released, runtime,
                        gender, director, poster, imdbRating)
                    VALUES(?,?,?,?,?,?,?,?)""",
                    (
                        title['Title'], title['Plot'], title['Released'],
                        title['Runtime'], title['Genre'], title['Director'],
                        title['Poster'], title['imdbRating']
                    ),
                )
                db.commit()
                error = "Movie Registered!"
            except KeyError as e:
                error = 'Movie not Found.'

        flash(error)
    return render_template('movies/register_movie.html')


@bp.route('/catalog', methods=('GET', 'POST'))
def catalog():
    db = get_db()
    
    movies = db.execute(
        'SELECT * FROM movies'
    ).fetchall()
    
    return render_template('movies/catalog.html', movies=movies)


@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request['title']
        director = request['director']
    
        db = get_db()
        
        db.execute(
            'SELECT * FROM movies WHERE title = ?, director = ?',
            (title, director),
        )    
