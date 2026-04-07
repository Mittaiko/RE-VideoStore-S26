"""
Movie_t.py

Test program for class Movie.

"""

import unittest

class Movie:
    """
    Enum for movie price codes.
    """
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        """
        Initialize a Movie object.

        Args:
            title (str): The title of the movie.
            price_code (int): The price code of the movie.
        """
        self._title = title
        self._price_code = price_code

    def get_title(self):
        """
        Get the title of the movie.

        Returns:
            str: The title of the movie.
        """
        return self._title

    def get_price_code(self):
        """
        Get the price code of the movie.

        Returns:
            int: The price code of the movie.
        """
        return self._price_code

    def set_price_code(self, price_code):
        """
        Set the price code of the movie.

        Args:
            price_code (int): The new price code of the movie.
        """
        self._price_code = price_code


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


if __name__ == "__main__":
    unittest.main()
