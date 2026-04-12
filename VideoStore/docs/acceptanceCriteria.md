# VideoStore Acceptance Criteria

## Overview

Each acceptance criterion below maps directly to a functional requirement in
`requirements.md`. The **Test** column identifies the test method that verifies
the criterion. Where no existing test covered a criterion, a new test is
specified and marked **[NEW]** — add these to the indicated test file.

---

## 1. Movie Management

### AC-1.1 — Three supported price categories
**Given** a movie is created with category `REGULAR`, `NEW_RELEASE`, or
`CHILDRENS`  
**When** `get_price_code()` is called  
**Then** it returns the corresponding integer constant

| Test file    | Test method                                          |
|--------------|------------------------------------------------------|
| `movie_t.py` | `test_regular_movie`                                 |
| `movie_t.py` | `test_new_release`                                   |
| `movie_t.py` | `test_childrens`                                     |

---

### AC-1.2 — Movie stores title and category
**Given** a movie is created with a title and a price category  
**When** `get_title()` and `get_price_code()` are called  
**Then** each returns the value supplied at construction

| Test file    | Test method                                          |
|--------------|------------------------------------------------------|
| `movie_t.py` | `test_regular_movie`                                 |
| `movie_t.py` | `test_longer_title`                                  |

---

### AC-1.3 — Price category can be changed
**Given** a movie exists with one price category  
**When** `set_price_code()` is called with a different valid category  
**Then** `get_price_code()` returns the new category

| Test file    | Test method                                          |
|--------------|------------------------------------------------------|
| `movie_t.py` | `test_change_price`                                  |
| `movie_t.py` | `test_set_price_code_changes_correctly`              |

---

### AC-1.4 — Invalid price category is rejected
**Given** a movie exists  
**When** `set_price_code()` is called with an unrecognised integer  
**Then** a `ValueError` is raised and the movie's category is unchanged

| Test file    | Test method                                          |
|--------------|------------------------------------------------------|
| `movie_t.py` | `test_invalid_price_code`                            |
| `movie_t.py` | `test_invalid_price_code_unchanged` **[NEW]**        |

```python
# movie_t.py
def test_invalid_price_code_unchanged(self):
    """Category must not change when an invalid code is supplied."""
    movie = Movie("A", Movie.REGULAR)
    try:
        movie.set_price_code(99)
    except ValueError:
        pass
    self.assertEqual(movie.get_price_code(), Movie.REGULAR)
```

---

### AC-1.5 — Internal price code is a Price object
**Given** a movie is created with any valid price category  
**When** the internal `_price_code` attribute is inspected  
**Then** it is an instance of `Price`, not a raw integer

| Test file    | Test method                                          |
|--------------|------------------------------------------------------|
| `movie_t.py` | `test_price_code_type_is_price`                      |

---

## 2. Rental Management

### AC-2.1 — Rental links a movie and a day count
**Given** a rental is created with a movie and a number of days  
**When** `get_movie()` and `get_days_rented()` are called  
**Then** each returns the value supplied at construction

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_get_movie`                                    |
| `rental_t.py` | `test_get_days_rented`                              |

---

### AC-2.2 — Days rented is immutable
**Given** a rental has been created  
**When** the rental is inspected at any point  
**Then** `get_days_rented()` always returns the original value (no setter exists)

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_days_rented_immutable` **[NEW]**              |

```python
# rental_t.py
def test_days_rented_immutable(self):
    """Rental exposes no method to change the days rented."""
    rental = Rental(Movie("A", Movie.REGULAR), 5)
    self.assertFalse(hasattr(rental, 'set_days_rented'),
                     "Rental must not expose a days setter")
    self.assertEqual(rental.get_days_rented(), 5)
```

---

### AC-2.3 — Customer starts with no rentals
**Given** a new customer is created  
**When** `statement()` is called immediately  
**Then** the statement reflects zero rentals, zero charge, zero points

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental`                                  |

---

### AC-2.4 — Rentals are added individually and accumulate
**Given** a customer exists  
**When** one rental is added and then a second rental is added  
**Then** the statement reflects both rentals

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_one_rental`                                 |
| `customer_t.py` | `test_two_rentals`                                |

---

### AC-2.5 — Rental cannot be removed once added
**Given** a customer has one or more rentals  
**When** the customer object is inspected  
**Then** no method exists to remove a rental

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_remove_rental` **[NEW]**                 |

```python
# customer_t.py
def test_no_remove_rental(self):
    """Customer must not expose a method to remove a rental."""
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("A", Movie.REGULAR), 1))
    self.assertFalse(hasattr(customer, 'remove_rental'),
                     "Customer must not expose a remove_rental method")
```

---

## 3. Charge Calculation

### AC-3.1a — Regular movie charge: flat rate for 1–2 days
**Given** a Regular movie rented for 1 or 2 days  
**When** `get_charge()` is called  
**Then** the charge is $2.00

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_regular_short`                                |
| `rental_t.py` | `test_regular_boundary`                             |
| `movie_t.py`  | `test_get_charge_regular_short`                     |

---

### AC-3.1b — Regular movie charge: extra days beyond 2
**Given** a Regular movie rented for more than 2 days  
**When** `get_charge()` is called  
**Then** the charge is $2.00 plus $1.50 for each day beyond 2

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_regular_boundary_plus_one`                    |
| `rental_t.py` | `test_regular_long`                                 |
| `rental_t.py` | `test_regular_many_days`                            |
| `movie_t.py`  | `test_get_charge_regular_long`                      |

---

### AC-3.1c — New Release charge: $3.00 per day, no flat base
**Given** a New Release movie rented for any number of days  
**When** `get_charge()` is called  
**Then** the charge is $3.00 multiplied by the number of days

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_new_release_one_day`                          |
| `rental_t.py` | `test_new_release_two_days`                         |
| `rental_t.py` | `test_new_release_three_days`                       |
| `rental_t.py` | `test_new_release_many_days`                        |
| `movie_t.py`  | `test_get_charge_new_release`                       |

---

### AC-3.1d — Children's movie charge: flat rate for 1–3 days
**Given** a Children's movie rented for 1, 2, or 3 days  
**When** `get_charge()` is called  
**Then** the charge is $1.50

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_childrens_short`                              |
| `rental_t.py` | `test_childrens_boundary`                           |
| `movie_t.py`  | `test_get_charge_childrens_boundary`                |

---

### AC-3.1e — Children's movie charge: extra days beyond 3
**Given** a Children's movie rented for more than 3 days  
**When** `get_charge()` is called  
**Then** the charge is $1.50 plus $1.50 for each day beyond 3

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_childrens_boundary_plus_one`                  |
| `rental_t.py` | `test_childrens_long`                               |
| `rental_t.py` | `test_childrens_many_days`                          |
| `movie_t.py`  | `test_get_charge_childrens_long`                    |

---

### AC-3.2 — Total charge is the sum of all rental charges
**Given** a customer has two rentals  
**When** the statement is produced  
**Then** the total charge equals the sum of the individual rental charges

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_two_rentals`                                |
| `customer_t.py` | `test_total_charge_sum` **[NEW]**                 |

```python
# customer_t.py
def test_total_charge_sum(self):
    """Total charge must equal the sum of individual rental charges."""
    r1 = Rental(Movie("A", Movie.REGULAR), 4)     # 5.0
    r2 = Rental(Movie("B", Movie.NEW_RELEASE), 2) # 6.0
    customer = Customer("Fred")
    customer.add_rental(r1)
    customer.add_rental(r2)
    expected_total = r1.get_charge() + r2.get_charge()
    statement = customer.statement()
    total_line = [l for l in statement.splitlines()
                  if l.startswith("Amount owed")][0]
    self.assertIn(str(expected_total).rstrip('0').rstrip('.'), total_line)
```

---

### AC-3.3 — Charges are formatted without trailing zeros
**Given** a charge has no meaningful decimal places (e.g. $2.00 or $14.00)  
**When** it appears in the statement  
**Then** trailing zeros and unnecessary decimal points are stripped (e.g. `2`, `14`)

**Given** a charge has one meaningful decimal place (e.g. $4.50)  
**When** it appears in the statement  
**Then** it appears as `4.5`, not `4.50`

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_one_rental` (checks against `.onerental.txt`) |
| `customer_t.py` | `test_two_rentals` (checks against `.tworental.txt`) |
| `customer_t.py` | `test_charge_formatting` **[NEW]**                |

```python
# customer_t.py
def test_charge_formatting(self):
    """Charges must strip trailing zeros in the statement."""
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("A", Movie.REGULAR), 1))   # 2 -> "2"
    customer.add_rental(Rental(Movie("B", Movie.CHILDRENS), 5)) # 4.5 -> "4.5"
    statement = customer.statement()
    self.assertIn("\tA\t2\n", statement)
    self.assertIn("\tB\t4.5\n", statement)
    self.assertNotIn("2.0", statement)
    self.assertNotIn("4.50", statement)
```

---

## 4. Frequent Renter Points

### AC-4.1 — Every rental earns at least one point
**Given** a rental of any movie category for any number of days  
**When** `get_frequent_renter_points()` is called  
**Then** it returns at least 1

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_frequent_renter_points_regular`               |
| `rental_t.py` | `test_frequent_renter_points_childrens`             |
| `rental_t.py` | `test_frequent_renter_points_new_release_one_day`   |
| `rental_t.py` | `test_one_day_all_types`                            |

---

### AC-4.2 — New Release rented for more than one day earns a bonus point
**Given** a New Release movie rented for more than 1 day  
**When** `get_frequent_renter_points()` is called  
**Then** it returns 2

**Given** a New Release movie rented for exactly 1 day  
**When** `get_frequent_renter_points()` is called  
**Then** it returns 1 (no bonus)

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_frequent_renter_points_new_release_bonus`     |
| `rental_t.py` | `test_frequent_renter_points_new_release_one_day`   |

---

### AC-4.3 — Points accumulate correctly across multiple rentals
**Given** a customer has two rentals, one of which is a multi-day New Release  
**When** the statement is produced  
**Then** the total points equals the sum of each rental's individual points

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_two_rentals`                                |
| `customer_t.py` | `test_points_accumulation` **[NEW]**              |

```python
# customer_t.py
def test_points_accumulation(self):
    """Points must be summed correctly across all rentals."""
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("A", Movie.NEW_RELEASE), 3))  # 2 pts
    customer.add_rental(Rental(Movie("B", Movie.REGULAR), 5))      # 1 pt
    customer.add_rental(Rental(Movie("C", Movie.CHILDRENS), 2))    # 1 pt
    statement = customer.statement()
    self.assertIn("You earned: 4 frequent renter points", statement)
```

---

## 5. Customer Statement

### AC-5.1 — Statement is produced on demand
**Given** a customer with any number of rentals  
**When** `statement()` is called  
**Then** it returns a non-empty string

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental`                                  |
| `customer_t.py` | `test_one_rental`                                 |
| `customer_t.py` | `test_statement_returns_string` **[NEW]**         |

```python
# customer_t.py
def test_statement_returns_string(self):
    """statement() must return a non-empty string."""
    customer = Customer("Fred")
    result = customer.statement()
    self.assertIsInstance(result, str)
    self.assertGreater(len(result), 0)
```

---

### AC-5.2 — Statement header contains customer name
**Given** a customer named X  
**When** `statement()` is called  
**Then** the first line is exactly `Rental Record for X`

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental`                                  |
| `customer_t.py` | `test_statement_header` **[NEW]**                 |

```python
# customer_t.py
def test_statement_header(self):
    """First line of statement must match the header format exactly."""
    customer = Customer("Alice")
    first_line = customer.statement().splitlines()[0]
    self.assertEqual(first_line, "Rental Record for Alice")
```

---

### AC-5.3 — Statement lists one line per rental with title and charge
**Given** a customer has one or more rentals  
**When** `statement()` is produced  
**Then** each rental appears on its own line as `\t<title>\t<charge>`

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_one_rental`                                 |
| `customer_t.py` | `test_two_rentals`                                |

---

### AC-5.4 — Statement total line is present and correct
**Given** a customer with any rentals  
**When** `statement()` is produced  
**Then** a line matching `Amount owed is: <total>` is present

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental`                                  |
| `customer_t.py` | `test_one_rental`                                 |
| `customer_t.py` | `test_two_rentals`                                |

---

### AC-5.5 — Statement points line is present and correct
**Given** a customer with any rentals  
**When** `statement()` is produced  
**Then** a line matching `You earned: <n> frequent renter points` is present

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental`                                  |
| `customer_t.py` | `test_one_rental`                                 |
| `customer_t.py` | `test_two_rentals`                                |

---

### AC-5.6 — Zero-rental statement is well-formed
**Given** a customer with no rentals  
**When** `statement()` is produced  
**Then** it matches the expected output exactly (header + `0` total + `0` points)

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental` (literal string + file compare)  |

---

## 6. Constraints

### AC-6.1 — Customer is identified by name
**Given** a customer is created with a given name  
**When** `get_name()` is called  
**Then** it returns exactly the name provided at construction

| Test file       | Test method                                       |
|-----------------|---------------------------------------------------|
| `customer_t.py` | `test_no_rental`                                  |
| `customer_t.py` | `test_one_rental`                                 |

---

### AC-6.2 — No data persists between runs
This is an architectural constraint verified by design inspection rather than
an automated test. The system holds no file I/O, database connections, or
global mutable state beyond what is created within a single execution.

| Verification | Method                                            |
|--------------|---------------------------------------------------|
| Code review  | Confirm no persistence layer exists in any module |

---

### AC-6.3 — Days rented is not validated for positivity
**Given** a rental is created with zero or negative days  
**When** `get_charge()` is called  
**Then** the system does not raise an exception (behaviour is undefined but
must not crash)

| Test file     | Test method                                         |
|---------------|-----------------------------------------------------|
| `rental_t.py` | `test_zero_days_no_crash` **[NEW]**                 |

```python
# rental_t.py
def test_zero_days_no_crash(self):
    """System must not crash on zero days (behaviour is undefined per FR-6.3)."""
    rental = Rental(Movie("A", Movie.REGULAR), 0)
    try:
        charge = rental.get_charge()
        self.assertIsInstance(charge, (int, float))
    except Exception as e:
        self.fail(f"get_charge() raised unexpectedly on zero days: {e}")
```

---

### AC-6.4 — No rental removal is supported
Already covered by AC-2.5 above.

---

## Summary of New Tests to Add

| Test file       | New test method                       | Covers  |
|-----------------|---------------------------------------|---------|
| `movie_t.py`    | `test_invalid_price_code_unchanged`   | AC-1.4  |
| `customer_t.py` | `test_no_remove_rental`               | AC-2.5  |
| `customer_t.py` | `test_total_charge_sum`               | AC-3.2  |
| `customer_t.py` | `test_charge_formatting`              | AC-3.3  |
| `customer_t.py` | `test_points_accumulation`            | AC-4.3  |
| `customer_t.py` | `test_statement_returns_string`       | AC-5.1  |
| `customer_t.py` | `test_statement_header`               | AC-5.2  |
| `rental_t.py`   | `test_days_rented_immutable`          | AC-2.2  |
| `rental_t.py`   | `test_zero_days_no_crash`             | AC-6.3  |
