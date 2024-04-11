import os
import requests
from dotenv import load_dotenv

load_dotenv()


# home
def test_home():
    res = requests.get('http://127.0.0.1:5000/')
    assert res.status_code == 200


# auth
def test_register():
    res = requests.get('http://127.0.0.1:5000/auth/register')
    assert res.status_code == 200


def test_login():
    res = requests.get('http://127.0.0.1:5000/auth/login')
    assert res.status_code == 200


# movies
def test_catalog():
    res = requests.get('http://127.0.0.1:5000/movies/catalog')
    assert res.status_code == 200


def test_search():
    res = requests.get('http://127.0.0.1:5000/movies/search')
    assert res.status_code == 200


def test_register_movie():
    user = {
        'email': os.getenv('USER_EMAIL'),
        'password': os.getenv('PASSWORD'),
    }

    with requests.post('http://127.0.0.1:5000/auth/login', data=user) as sess:
        res = requests.get('http://127.0.0.1:5000/movies/register')
        assert sess.status_code == 200
        assert res.status_code == 200
