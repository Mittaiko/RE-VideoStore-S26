## Question 3
Determining the frequent renter points should probably be a responsibility of class ```Rental``` rather than class ```Customer```.  Using a _Extract method_ refactoring, create a new method ```getFrequentRenterPoints``` in class ```Rental``` and call it in method ```statement``` to get the frequent renter points.


**Start Day/Time:**  04/09/2026 4:41pm

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

The AI’s output was useful because it correctly identified that the frequent renter points logic should be moved from the Customer class into the Rental class, which matched the refactoring requirement. It was also correct in explaining the new method structure and how Customer should delegate the calculation instead of handling it directly. However, I had to verify the explanation against my own code because the AI was describing the original state of the assignment rather than my updated implementation. Overall, the guidance was appropriate but required me to confirm what was already implemented in my project.

**What changes did you make to the AI‑generated material? Be specific.**

I followed the AI’s suggestion to create the get_frequent_renter_points() method in the Rental class, but I adjusted the implementation to match my existing code style using getter methods (get_movie() and get_days_rented()). I also ensured that Customer only calls rental.get_frequent_renter_points() instead of containing any conditional logic. I also debugged file path issues separately, since the AI explanation did not relate to the missing .txt file error I encountered.

**I copied my AI-assisted chat log to ./docs/log3.txt**
[X] Yes [ ] No 

**Difficulty Level:**
[ ] Easy  [X] Avg  [ ] Difficult

**End Day/Time:** 04/09/2026 5:36pm

