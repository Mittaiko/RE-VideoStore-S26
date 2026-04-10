## Question 5
The method ```getCharge``` in class ```Rental``` accesses more information in class ```Movie``` than it does in class ```Rental```.  This is a classic symptom of a method that is in the wrong place.  Perform a _Move Method_ refactoring to move the functionality of the method ```getCharge``` into a new method of the same name in the class ```Movie```.  Leave the method ```getCharge``` in class ```Rental``` and have it call the new method in class ```Movie```.  It will be necessary to pass the number of days rented.

**Start Day/Time:** 10:30am 04/10/2026

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

The AI’s output was useful because it identified that the charge calculation logic relied more on the Movie class than on the Rental class. The AI suggested moving the pricing logic into a new get_charge() method in the Movie class and having the Rental class delegate to that method by passing the number of days rented. I evaluated whether the output was appropriate by comparing it with the existing code and verifying that the behavior of the program remained the same after the refactoring. I also ran the existing unit tests (Customer_t.py, Rental_t.py, and Movie_t.py) to ensure that the output of the program did not change after the refactoring.

**What changes did you make to the AI‑generated material? Be specific.**

I followed the AI’s suggestion to move the charge calculation logic into a new get_charge(days_rented) method inside the Movie class. During testing, I discovered an issue where the test file contained its own Movie class definition, which prevented the tests from using the updated Movie class from Movie.py. I corrected this by importing the Movie class from Movie.py instead of redefining it in the test file. After making these adjustments, I reran the tests to confirm that all tests passed and that the refactoring preserved the program’s behavior.

**I copied my AI-assisted chat log to ./docs/log5.txt**
[X] Yes [ ] No 

**Difficulty Level:**
[ ] Easy  [X] Avg  [ ] Difficult

**End Day/Time:** 04/10/2026 11:30am

