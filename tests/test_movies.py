# flake8: noqa
import unittest

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from movedbymovies import create_app


class TestMovies(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.test_client = self.app.test_client()
        
    
    def test_movie_search_by_title(self):
        res = self.test_client.post('/movies/search', data={'movie-title': 'mr. robot', 'year': '', 'director': ''})
        self.assertIn('Mr. Robot', res.text)
        self.assertIn('24 Jun 2015', res.text)
        self.assertIn('49 min', res.text)
        self.assertIn('Crime, Drama, Thriller', res.text)
        self.assertEqual(res.status_code, 200)

    def test_movie_search_by_year(self):
        res = self.test_client.post('/movies/search', data={'movie-title': '', 'year': '2001', 'director': ''})
        self.assertIn('Hedwig', res.text)
        self.assertIn('31 Aug 2001', res.text)
        self.assertIn('95 min', res.text)
        self.assertIn('Comedy, Drama, Music', res.text)
        self.assertEqual(res.status_code, 200)

    def test_movie_search_by_director(self):
        res = self.test_client.post('/movies/search', data={'movie-title': '', 'year': '', 'director': 'John Cameron Mitchell'})
        self.assertIn('Hedwig', res.text)
        self.assertIn('31 Aug 2001', res.text)
        self.assertIn('95 min', res.text)
        self.assertIn('Comedy, Drama, Music', res.text)
        self.assertEqual(res.status_code, 200)
