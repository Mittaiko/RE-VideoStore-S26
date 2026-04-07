# VideoStore.py

# Basic operations of a video store.

from Movie import Movie
from Rental import Rental
from Customer import Customer

def main():
    # Create movies
    lotr = Movie("Lord of the Rings", Movie.REGULAR)
    hp = Movie("Harry Potter", Movie.CHILDRENS)

    # Create rentals of these movies
    r1 = Rental(lotr, 10)
    r2 = Rental(hp, 5)

    # Create a customer with some rentals
    customer = Customer("Fred")
    customer.add_rental(r1)
    customer.add_rental(r2)

    # Output Fred's statement
    print(customer.statement())

if __name__ == "__main__":
    main()
