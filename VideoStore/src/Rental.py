# Rental.py

# Include necessary dependencies

from Movie import Movie

class Rental:
    def __init__(self, movie, days_rented):
        """
        Constructor for Rental class.

        :param movie: Movie object representing the rented movie.
        :param days_rented: Integer representing the number of days the movie is rented.
        """
        self._movie = movie
        self._days = days_rented

    def get_days_rented(self):
        """
        Get the number of days the movie is rented.

        :return: Integer representing the number of days rented.
        """
        return self._days

    def get_movie(self):
        """
        Get the movie object that is rented.

        :return: Movie object representing the rented movie.
        """
        return self._movie

    def get_charge(self) -> float:
        """Delegates charge calculation to Movie, passing days rented."""
        return self._movie.get_charge(self._days)
    
    def get_frequent_renter_points(self) -> int:
        """Returns frequent renter points earned for this rental.
        New releases rented for more than one day earn a bonus point."""
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            return 2
        return 1
