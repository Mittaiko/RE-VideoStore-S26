## Question 6
When creating a hierarchy for common behavior, it is common to use an abstract class that does not have any implementation for its methods.  It serves as the base class for a hierarchy.  Add an abstract class ```Price``` in ```Movie```.  This will serve as a base class for new classes and is the start of the _Replace Type Code with State/Strategy_ Refactoring

(Currently the price code is an ```int```.  We will need to move from an ```int``` to type ```Price``` later.  Nothing to change yet.)

Define in ```Movie``` the following classes: ```RegularPrice```, ```ChildrensPrice```, and ```NewReleasePrice```.  Have all of them inherit from the class ```Price```.

Declare a pure virtual method ```getPriceCode``` in class ```Price```.  Define a virtual method ```getPriceCode``` in each of the subclasses that returns the corresponding category (e.g., ```Movie::CHILDREN``` for the class ```ChildrensPrice```).

(Note: Pure virtual functions are not supported in Python but you can mimic it. Think about how you would do it.)

**Start Day/Time:**  04/10/2026 12:09pm

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

I checked the AI’s answer and compared it with the instructions to the assignment. The assignment asked to create an abstract class called Price and three subclasses. The response followed the requirements and used Python’s abc module with ABC and @abstractmethod to mimic a virtual method, which fits Python’s way of implementing abstract classes. I also ran the existing tests to make sure that nothing else in the program was broken since the assignment stated that the price code should still remain an integer for now.

**What changes did you make to the AI‑generated material? Be specific.**

I added additional unit tests to verify the new classes worked correctly. These tests checked that each subclass returned the correct price code, that the Price class could not be instantiated directly because it is abstract, and that each subclass was an instance of the Price base class. These tests helped confirm that the new hierarchy was implemented correctly while keeping the existing functionality unchanged.

**I copied my AI-assisted chat log to ./docs/log6.txt**
[X] Yes [ ] No 

**Difficulty Level:**
[ ] Easy  [X] Avg  [ ] Difficult

**End Day/Time:** 04/10/2026 12:32pm

