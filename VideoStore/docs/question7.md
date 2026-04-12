## Question 7
Now we need to make the changes that will use our new types for the method ```price_code``` in Movie.  Perform a type change.

Change the type of the variable ```price_code``` to ```Price```

Change the method ```setPriceCode``` to set the variable ```price_code``` to a new instance of the correct ```Price``` object using a switch or equivalent data structure in Python.

Change the method ```getPriceCode``` to call the method ```getPriceCode``` on the ```Price``` object and return that value.

**Start Day/Time:**  8:27pm 04/11/2026

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

I made sure that the AI’s response followed the required refactoring steps. The AI explained how to change the price_code variable from an integer to a Price object and how to update the set_price_code and get_price_code methods. After implementing the changes, I ran the unit tests and the additional unit tests to confirm that the program still worked correctly and that the new behavior matched the assignment requirements and saw no blockages.

**What changes did you make to the AI‑generated material? Be specific.**

I mostly followed the AI’s implementation and did not make many major changes. I also added the suggested unit tests to verify that invalid price codes raise an error and that the _price_code variable is now stored as a Price object instead of an integer.

**I copied my AI-assisted chat log to ./docs/log7.txt**
[X] Yes [ ] No 

**Difficulty Level:**
[ ] Easy  [X] Avg  [ ] Difficult

**End Day/Time:** 8:53pm 04/11/2026

