## Question 4
Loops that do more than one thing at a time are more difficult to comprehend and extend in the future.  The loop in method ```statement``` is performing multiple duties; including accumulating the total charge for all movies.  Perform a _Replace Temp with Query refactoring_ to eliminate the variable ```totalAmount``` by creating a private method ```getTotalCharge``` in class Customer.  Use a call to this new method where ```totalAmount``` is being output.

**Start Day/Time:**  04/09/2026 8:45pm

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

The AI’s output was useful because it identified that the totalAmount variable in the statement() method could be removed using a Replace Temp with Query refactoring. It explained how to move the total charge calculation into a separate helper method in the Customer class, which improved code readability and separation of concerns. I verified that the suggested change preserved the original output by running the existing unit tests and they all passed. The output was accurate in terms of behavior preservation, but I still needed to adjust the implementation slightly to better match my existing code style and avoid redundant method calls.

**What changes did you make to the AI‑generated material? Be specific.**

I followed the AI’s suggestion to create a private helper method (__get_total_charge) to compute the total rental charge separately from the loop in statement(). However, I modified the statement() method by storing rental.get_charge() in a temporary variable (charge) inside the loop. This change reduced duplicate method calls since get_charge() was previously being called multiple times per rental. I also ensured that the output formatting remained exactly the same so that all existing test cases continued to pass. It made it more efficient.

**I copied my AI-assisted chat log to ./docs/log4.txt**
[X] Yes [ ] No 

**Difficulty Level:**
[ ] Easy  [X] Avg  [ ] Difficult

**End Day/Time:** 04/09/2026 9:04pm

