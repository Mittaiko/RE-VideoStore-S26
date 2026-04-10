# Movie.py

# Class hierarchy for pricing strategy
from abc import ABC, abstractmethod

class Price(ABC):
    """
    Abstract base class for movie pricing strategies.
    """

    @abstractmethod
    def get_price_code(self) -> int:
        """
        Subclasses must return the corresponding price code.
        """
        raise NotImplementedError("Subclasses must implement get_price_code()")


class RegularPrice(Price):
    def get_price_code(self) -> int:
        return 0  # corresponds to Movie.REGULAR


class NewReleasePrice(Price):
    def get_price_code(self) -> int:
        return 1  # corresponds to Movie.NEW_RELEASE


class ChildrensPrice(Price):
    def get_price_code(self) -> int:
        return 2  # corresponds to Movie.CHILDRENS


class Movie:
    # Class constants for price codes
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        """
        Constructor to initialize movie title and price code
        """
        self._title = title
        self._price_code = price_code

    def get_title(self):
        """
        Getter for movie title
        """
        return self._title

    def get_price_code(self):
        """
        Getter for movie price code
        """
        return self._price_code

    def set_price_code(self, new_price_code):
        """
        Setter for movie price code
        """
        self._price_code = new_price_code

    def get_charge(self, days_rented: int) -> float:
        """
        Calculate the rental charge based on the movie's price code
        and the number of days rented.
        """
        this_amount = 0

        if self._price_code == Movie.REGULAR:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5

        elif self._price_code == Movie.NEW_RELEASE:
            this_amount += days_rented * 3

        elif self._price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5

        return this_amount
