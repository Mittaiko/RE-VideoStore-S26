# Customer_t.py
#
# Test program for class Customer.

import unittest
from Customer import Customer, Movie, Rental

class TestCustomer(unittest.TestCase):

    def test_no_rental(self):
        customer = Customer("Fred")
        self.assertEqual(customer.get_name(), "Fred")

        # test using literal string
        self.assertEqual(customer.statement(), "Rental Record for Fred\nAmount owed is: 0\nYou earned: 0 frequent renter points\n")

        # test using external file
        with open("Customer_t.norental.txt", "r") as finput:
            expected_output = finput.read()
        self.assertEqual(customer.statement(), expected_output)

    def test_one_rental(self):
        customer = Customer("Fred")
        self.assertEqual(customer.get_name(), "Fred")

        # one rental
        customer.add_rental(Rental(Movie("A", Movie.REGULAR), 1))

        # test using external file
        with open("Customer_t.onerental.txt", "r") as finput:
            expected_output = finput.read()
        self.assertEqual(customer.statement(), expected_output)

    def test_two_rentals(self):
        customer = Customer("Fred")

        # Create movies
        lotr = Movie("Lord of the Rings", Movie.REGULAR)
        hp = Movie("Harry Potter", Movie.CHILDRENS)

        # Create rentals of these movies
        r1 = Rental(lotr, 10)
        r2 = Rental(hp, 5)

        # add two rentals
        customer.add_rental(r1)
        customer.add_rental(r2)

        # test using external file
        with open("Customer_t.tworental.txt", "r") as finput:
            expected_output = finput.read()
        self.assertEqual(customer.statement(), expected_output)

if __name__ == "__main__":
    unittest.main()
