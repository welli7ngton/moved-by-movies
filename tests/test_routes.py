import requests


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
