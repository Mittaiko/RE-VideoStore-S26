## Question 6
When creating a hierarchy for common behavior, it is common to use an abstract class that does not have any implementation for its methods.  It serves as the base class for a hierarchy.  Add an abstract class ```Price``` in ```Movie```.  This will serve as a base class for new classes and is the start of the _Replace Type Code with State/Strategy_ Refactoring

(Currently the price code is an ```int```.  We will need to move from an ```int``` to type ```Price``` later.  Nothing to change yet.)

Define in ```Movie``` the following classes: ```RegularPrice```, ```ChildrensPrice```, and ```NewReleasePrice```.  Have all of them inherit from the class ```Price```.

Declare a pure virtual method ```getPriceCode``` in class ```Price```.  Define a virtual method ```getPriceCode``` in each of the subclasses that returns the corresponding category (e.g., ```Movie::CHILDREN``` for the class ```ChildrensPrice```).

(Note: Pure virtual functions are not supported in Python but you can mimic it. Think about how you would do it.)

**Start Day/Time:**  enter date and time here

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

write answer here

**What changes did you make to the AI‑generated material? Be specific.**

write answer here

**I copied my AI-assisted chat log to ./docs/log6.txt**
[ ] Yes [ ] No 

**Difficulty Level:**
[ ] Easy  [ ] Avg  [ ] Difficult

**End Day/Time:** enter date and time here

