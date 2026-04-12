# Movie.py

# Class hierarchy for pricing strategy
from abc import ABC, abstractmethod

class Price(ABC):
    """
    Abstract base class for movie pricing strategies.
    """

    @abstractmethod
    def get_price_code(self) -> int:
        """Pure virtual method — subclasses must implement this."""
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

    # Maps integer price codes to their corresponding Price objects
    _PRICE_MAP = None

    @classmethod
    def _get_price_map(cls) -> dict:
        """Lazily initialise the price map after all classes are defined."""
        if cls._PRICE_MAP is None:
            cls._PRICE_MAP = {
                cls.REGULAR:      RegularPrice(),
                cls.NEW_RELEASE:  NewReleasePrice(),
                cls.CHILDRENS:    ChildrensPrice(),
            }
        return cls._PRICE_MAP

    def __init__(self, title, price_code):
        """
        Constructor to initialize movie title and price code
        """
        self._title = title
        self._price_code = price_code
        self.set_price_code(price_code)

    def get_title(self):
        """
        Getter for movie title
        """
        return self._title

    def get_price_code(self):
        """
        Getter for movie price code
        """
        return self._price_code.get_price_code()

    def set_price_code(self, new_price_code: int):
        """Converts the integer price code to the correct Price object."""
        price_map = self._get_price_map()
        if new_price_code not in price_map:
            raise ValueError(f"Invalid price code: {new_price_code}")
        self._price_code = price_map[new_price_code]

    def get_charge(self, days_rented: int) -> float:
        """Calculate the rental charge based on this movie's price code
        and the number of days rented."""
        this_amount = 0
        if self.get_price_code() == Movie.REGULAR:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5
        elif self.get_price_code() == Movie.NEW_RELEASE:
            this_amount += days_rented * 3
        elif self.get_price_code() == Movie.CHILDRENS:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5
        return this_amount
