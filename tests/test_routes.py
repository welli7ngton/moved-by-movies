# flake8: noqa
import unittest

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from movedbymovies import create_app


class TestRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.test_client = self.app.test_client()

    def test_home(self):
        res = self.test_client.get('/')
        assert res.status_code == 200
        assert '<title> Home  - Moved By Movies</title>' in res.text

    def test_register_route(self):
        res = self.test_client.get('/auth/register')
        assert '<title>Register - Moved By Movies</title>' in res.text
        assert res.status_code == 200
    
    def test_login_route(self):
        res = self.test_client.get('/auth/login')
        assert '<title>Log In - Moved By Movies</title>' in res.text
        assert res.status_code == 200
        
    def test_catalog_route(self):
        res = self.test_client.get('/movies/catalog')
        assert '<title>Catalog - Moved By Movies</title>' in res.text
        assert res.status_code == 200

    def test_search(self):
        res = self.test_client.get('/movies/search')
        assert 'Search' in res.text
        assert res.status_code == 200

if __name__ == '__main__':
    unittest.main(verbosity=2)
