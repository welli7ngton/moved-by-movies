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
        movie_title = request.form['movie-name']

        db = get_db()
        error = None

        if not movie_title:
            error = 'Movie Title is required.'

        if error is None:
            response = requests.get(f'{HOST}?t={movie_title}&apikey={API_KEY}&plot=full')
            title = response.json()

            db.execute(
                """INSERT INTO movie
                    (title, plot, year,
                    released, runtime, gender,
                    director, poster, imdbRating)
                   VALUES(?,?,?,?,?,?,?,?,?)""",
                (
                    title['Title'], title['Plot'], title['Year'],
                    title['Released'], title['Runtime'], title['Genre'],
                    title['Director'], title['Poster'], title['imdbRating']
                ),
            )
            db.commit()
            error = "Movie Registered!"
        else:
            error = "Movie not found, sorry :("

        flash(error)
    return render_template('user_actions/register_movie.html')
