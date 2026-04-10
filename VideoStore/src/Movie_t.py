"""
Movie_t.py

Test program for class Movie.

"""

import unittest

from Movie import Movie

class TestMovie(unittest.TestCase):
    """
    Test cases for the Movie class.
    """

    def test_regular_movie(self):
        # regular movie
        movie = Movie("A", Movie.REGULAR)
        self.assertEqual(movie.get_title(), "A")
        self.assertEqual(movie.get_price_code(), Movie.REGULAR)

    def test_new_release(self):
        # new release
        movie = Movie("A", Movie.NEW_RELEASE)
        self.assertEqual(movie.get_title(), "A")
        self.assertEqual(movie.get_price_code(), Movie.NEW_RELEASE)

    def test_childrens(self):
        # childrens
        movie = Movie("A", Movie.CHILDRENS)
        self.assertEqual(movie.get_title(), "A")
        self.assertEqual(movie.get_price_code(), Movie.CHILDRENS)

    def test_longer_title(self):
        # longer title
        movie = Movie("A B", Movie.REGULAR)
        self.assertEqual(movie.get_title(), "A B")
        self.assertEqual(movie.get_price_code(), Movie.REGULAR)

    def test_change_price(self):
        # change price
        movie = Movie("A", Movie.NEW_RELEASE)
        self.assertEqual(movie.get_title(), "A")
        self.assertEqual(movie.get_price_code(), Movie.NEW_RELEASE)
        movie.set_price_code(Movie.REGULAR)
        self.assertEqual(movie.get_price_code(), Movie.REGULAR)

    # new tests for get_charge method
    def test_get_charge_regular_short(self):
        movie = Movie("A", Movie.REGULAR)
        self.assertAlmostEqual(movie.get_charge(1), 2.0)

    def test_get_charge_regular_long(self):
        movie = Movie("A", Movie.REGULAR)
        self.assertAlmostEqual(movie.get_charge(4), 5.0)

    def test_get_charge_new_release(self):
        movie = Movie("A", Movie.NEW_RELEASE)
        self.assertAlmostEqual(movie.get_charge(3), 9.0)

    def test_get_charge_childrens_boundary(self):
        movie = Movie("A", Movie.CHILDRENS)
        self.assertAlmostEqual(movie.get_charge(3), 1.5)

    def test_get_charge_childrens_long(self):
        movie = Movie("A", Movie.CHILDRENS)
        self.assertAlmostEqual(movie.get_charge(6), 6.0)

if __name__ == "__main__":
    unittest.main()
