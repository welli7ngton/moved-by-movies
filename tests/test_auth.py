# flake8: noqa
import unittest


import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from movedbymovies import create_app


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.test_client = self.app.test_client()
        self.user_data = {
                "username": "test",
                "email": "test@test.com",
                "birth": "01-01-1001",
            }

    def test_auth_password_has_no_punctuation(self):
        self.user_data.update({
            "password": "Str0ngPass",
            "confirm-password": "Str0ngPass",
            })

        with self.test_client as c:
            res = c.post('/auth/register',data=self.user_data)
            self.assertIn(b'flash', res.data)
            self.assertEqual(res.status_code, 200)

    def test_auth_password_has_no_numbers(self):
        self.user_data.update({
            "password": "strOngpass!",
            "confirm-password": "strOngpass!",
        })

        with self.test_client as c:
            res = c.post('/auth/register',data=self.user_data)
            self.assertIn(b'flash', res.data)
            self.assertEqual(res.status_code, 200)

    def test_auth_password_has_no_enough_length(self):
        self.user_data.update({
                "password": "Str0!",
                "confirm-password": "Str0!",
            })

        with self.test_client as c:
            res = c.post('/auth/register',data=self.user_data)
            self.assertIn(b'flash', res.data)
            self.assertEqual(res.status_code, 200)

    def test_auth_password_has_no_uppercase(self):
        self.user_data.update({
                "password": "str0ngpass!",
                "confirm-password": "str0ngpass!",
            }) 

        with self.test_client as c:
            res = c.post('/auth/register',data=self.user_data)
            self.assertIn(b'flash', res.data)
            self.assertEqual(res.status_code, 200)
    
    def test_user_email_already_exists(self):
        self.user_data.update({
            "email": "wellington@admin.com",
            "password": "str0ngPass!",
            "confirm-password": "str0ngPass!",
        })
        
        with self.test_client as c:
            res = c.post('/auth/register', data=self.user_data)
            self.assertIn(b'flash', res.data)
            self.assertEqual(res.status_code, 200)
    
    def test_fail_login_error_email(self):
        data ={
            "password": "1AmStr0ng!",
            "email": "test@not_exists.com",
        }
        
        with self.test_client as c:
            res = c.post('/auth/login', data=data)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'flash', res.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
