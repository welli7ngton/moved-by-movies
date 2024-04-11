# flake8:noqa
import requests


def test_register_post():
    data_json = {
        'username': 'test',
        'email': 'testing1@test.com',
        'password': '1AmStr0ng!',
        'confirm-password': '1AmStr0ng!',
        'birth': '2000-01-01'
    }
    res = requests.post('http://127.0.0.1:5000/auth/register', data=data_json)
    assert res.status_code == 200


def test_register_post_get_an_PasswordHasNoPunctuation_error():
    data_json = {
        'username': 'test',
        'email': 'testing1@test.com',
        'password': '1AmStr0ng',
        'confirm-password': '1AmStr0ng',
        'birth': '2000-01-01'
    }
    res = requests.post('http://127.0.0.1:5000/auth/register', data=data_json)
    assert res.json() == {"error": "Password has no punctuation(!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)"}
    assert res.status_code == 200


def test_register_post_get_an_HasNoNumbers_error():
    data_json = {
        'username': 'test',
        'email': 'testing1@test.com',
        'password': 'IAmStrOng!',
        'confirm-password': 'IAmStrOng!',
        'birth': '2000-01-01'
    }
    res = requests.post('http://127.0.0.1:5000/auth/register', data=data_json)
    assert res.json() == {"error": "Password has no numbers (0123456789)"}
    assert res.status_code == 200


def test_register_post_get_an_HasNotEnoughLength_error():
    data_json = {
        'username': 'test',
        'email': 'testing1@test.com',
        'password': '1!Qa',
        'confirm-password': '1!Qa',
        'birth': '2000-01-01'
    }
    res = requests.post('http://127.0.0.1:5000/auth/register', data=data_json)
    assert res.json() == {"error": "Password has no enough length(8)"}
    assert res.status_code == 200


def test_register_post_get_an_HasNoUppercase_error():
    data_json = {
        'username': 'test',
        'email': 'testing1@test.com',
        'password': '1!qazwsx',
        'confirm-password': '1!qazwsx',
        'birth': '2000-01-01'
    }
    res = requests.post('http://127.0.0.1:5000/auth/register', data=data_json)
    assert res.json() == {"error": "Password has no uppercase(ABCDEFGHIJKLMNOPQRSTUVWXYZ)"}
    assert res.status_code == 200
