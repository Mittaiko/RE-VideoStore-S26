# VideoStore Functional Requirements

## Overview

The VideoStore system manages movie rentals for customers. It tracks which movies a customer has rented, calculates charges based on movie type and rental duration, awards frequent renter points, and produces a printed statement summarizing all activity for a given customer.

---

## 1. Movie Management

**FR-1.1** The system shall support three categories of movies: Regular, New Release, and Children's.

**FR-1.2** Each movie shall have a title and a price category.

**FR-1.3** The system shall allow a movie's price category to be changed after the movie has been created.

**FR-1.4** The system shall reject any attempt to assign an unrecognised price category to a movie.

---

## 2. Rental Management

**FR-2.1** A rental shall associate exactly one movie with a number of days rented.

**FR-2.2** The number of days rented shall be set at the time the rental is created and shall not change.

**FR-2.3** A customer may have zero or more rentals associated with their account.

**FR-2.4** Rentals shall be added to a customer's account one at a time.

---

## 3. Charge Calculation

**FR-3.1** The system shall calculate a rental charge for each rental based on the movie's price category and the number of days rented, according to the following rules:

| Category    | Base Charge | Extra Charge                              |
|-------------|-------------|-------------------------------------------|
| Regular     | $2.00       | $1.50 per day beyond 2 days              |
| New Release | —           | $3.00 per day (no flat base)             |
| Children's  | $1.50       | $1.50 per day beyond 3 days              |

**FR-3.2** The system shall calculate a total charge across all of a customer's rentals.

**FR-3.3** Charges shall be represented as floating-point values and displayed without unnecessary trailing zeros (e.g. `4.5` not `4.50`, `2` not `2.00`).

---

## 4. Frequent Renter Points

**FR-4.1** Every rental shall earn the customer at least one frequent renter point, regardless of movie category or days rented.

**FR-4.2** A New Release rented for more than one day shall earn one additional bonus frequent renter point, for a total of two points.

**FR-4.3** The system shall accumulate frequent renter points across all of a customer's rentals and report the total.

---

## 5. Customer Statement

**FR-5.1** The system shall produce a plain-text rental statement for a given customer on demand.

**FR-5.2** The statement shall begin with a header line in the format:
```
Rental Record for <customer name>
```

**FR-5.3** The statement shall list one line per rental in the format:
```
	<movie title>	<charge>
```
where the charge is formatted per FR-3.3.

**FR-5.4** The statement shall include a total amount owed line in the format:
```
Amount owed is: <total charge>
```

**FR-5.5** The statement shall include a frequent renter points line in the format:
```
You earned: <points> frequent renter points
```

**FR-5.6** A statement produced for a customer with no rentals shall still include the header, a total of `0`, and a points total of `0`.

---

## 6. Constraints and Assumptions

**FR-6.1** A customer is identified by name only. The system does not manage unique customer IDs.

**FR-6.2** The system does not persist any data between executions. All movies, rentals, and customers exist only for the duration of a single run.

**FR-6.3** The system does not validate that the number of days rented is a positive integer. Callers are responsible for passing valid values.

**FR-6.4** The system does not support removing a rental from a customer's account once it has been added.

---

## Traceability to Source Code

| Requirement | Class / Method                          |
|-------------|-----------------------------------------|
| FR-1.1–1.4  | `Movie`, `Price`, `RegularPrice`, `NewReleasePrice`, `ChildrensPrice` |
| FR-2.1–2.4  | `Rental.__init__`, `Customer.add_rental` |
| FR-3.1–3.3  | `Movie.get_charge`, `Customer.__get_total_charge` |
| FR-4.1–4.3  | `Rental.get_frequent_renter_points`, `Customer.statement` |
| FR-5.1–5.6  | `Customer.statement`                    |
| FR-6.1–6.4  | System-wide (design constraints)        |
