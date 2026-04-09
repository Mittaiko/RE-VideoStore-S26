"""
Rental_t.py

Test program for class Rental

"""

# Assuming the Rental class is defined in a module named Rental
import unittest
from Rental import Rental
from Movie import Movie

class TestRental(unittest.TestCase):

    def test_regular_short(self):
        # Regular movie, 1 day (flat rate, no extra charge)
        movie = Movie("A", Movie.REGULAR)
        rental = Rental(movie, 1)
        self.assertEqual(rental.get_movie(), movie)
        self.assertEqual(rental.get_days_rented(), 1)
        self.assertAlmostEqual(rental.get_charge(), 2.0)

    def test_regular_long(self):
        # Regular movie, 4 days (2 base + 2 extra days * 1.5)
        movie = Movie("A", Movie.REGULAR)
        rental = Rental(movie, 4)
        self.assertAlmostEqual(rental.get_charge(), 5.0)

    def test_regular_boundary(self):
        # Regular movie, exactly 2 days — boundary, no extra charge yet
        movie = Movie("A", Movie.REGULAR)
        rental = Rental(movie, 2)
        self.assertAlmostEqual(rental.get_charge(), 2.0)

    def test_new_release_one_day(self):
        # New release, 1 day (1 * 3)
        movie = Movie("B", Movie.NEW_RELEASE)
        rental = Rental(movie, 1)
        self.assertAlmostEqual(rental.get_charge(), 3.0)

    def test_new_release_three_days(self):
        # New release, 3 days (3 * 3)
        movie = Movie("B", Movie.NEW_RELEASE)
        rental = Rental(movie, 3)
        self.assertAlmostEqual(rental.get_charge(), 9.0)

    def test_childrens_short(self):
        # Children's movie, 2 days (flat rate, no extra charge)
        movie = Movie("C", Movie.CHILDRENS)
        rental = Rental(movie, 2)
        self.assertAlmostEqual(rental.get_charge(), 1.5)

    def test_childrens_boundary(self):
        # Children's movie, exactly 3 days — boundary, no extra charge yet
        movie = Movie("C", Movie.CHILDRENS)
        rental = Rental(movie, 3)
        self.assertAlmostEqual(rental.get_charge(), 1.5)

    def test_childrens_long(self):
        # Children's movie, 6 days (1.5 base + 3 extra days * 1.5)
        movie = Movie("C", Movie.CHILDRENS)
        rental = Rental(movie, 6)
        self.assertAlmostEqual(rental.get_charge(), 6.0)

    def test_get_movie(self):
        # Verify get_movie returns the correct Movie object
        movie = Movie("Lord of the Rings", Movie.REGULAR)
        rental = Rental(movie, 5)
        self.assertEqual(rental.get_movie(), movie)
        self.assertEqual(rental.get_movie().get_title(), "Lord of the Rings")

    def test_get_days_rented(self):
        # Verify get_days_rented returns the correct value
        movie = Movie("A", Movie.NEW_RELEASE)
        rental = Rental(movie, 7)
        self.assertEqual(rental.get_days_rented(), 7)

if __name__ == "__main__":
    unittest.main()
    
