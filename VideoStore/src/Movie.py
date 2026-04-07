# Movie.py

# Class for Movie

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

