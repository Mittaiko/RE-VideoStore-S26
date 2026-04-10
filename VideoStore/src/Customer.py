# Customer.py

# Definition file for Customer class.

from typing import List
from Rental import Rental
from Movie import Movie

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.rentals: List[Rental] = []

    def get_name(self) -> str:
        return self.name

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def __get_total_charge(self) -> float:
        """Computes the total charge across all rentals."""
        total = 0.0
        for rental in self.rentals:
            total += rental.get_charge()
        return total

    def statement(self) -> str:
        result = f"Rental Record for {self.get_name()}\n"
        frequent_renter_points = 0
        for rental in self.rentals:
            charge = rental.get_charge()
            frequent_renter_points += rental.get_frequent_renter_points()
            result += f"\t{rental.get_movie().get_title()}\t" + f"{charge:.2f}".rstrip('0').rstrip('.') + "\n"
        result += f"Amount owed is: {f'{self.__get_total_charge():.2f}'.rstrip('0').rstrip('.')}\n"
        result += f"You earned: {frequent_renter_points} frequent renter points\n"
        return result
