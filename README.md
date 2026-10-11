# Student Information 
**Name :** Mehlike Rana Şahin
**Student Number:** 2304109035
**Department:** Management Information Systems
**Course Name:** MIS203 - Basic Programming

...

### AI Assistance Details
**AI Tool Used:** Gemini
**Prompt Used:** "Write a simple python script that takes user input for name, age, and career goal, then prints them in a formatted student profile."
**What did you change?:** I added custom prompt text inside the 'input()' functions to make the terminal messages clear for the user.

# WEEK 02#
AI Tool Used: Gemini
How can I writw a python grade calculator with a while loop, continue for invalide socre, and break on quit?
What did you change: I used :.2f to show average score with just two decimal places.
What does break do in your program: It stops the infinite loop immediately when q is entered so the program can calculate and print the final stats.

# WEEK 03#
AI Tool Used: Gemini

Prompt Used: Create a Python program that calculates cinema ticket prices, including age and student discounts, using loops and conditional statements.

What did you cahnge: I used a `try-except` block to prevent the program from crashing if a user enters letters instead of numbers for the age input. I also applied the `.lower()` method to standardise string inputs like student status and day type regardless of letter case.
Tests:
1. Boundary Age Test (Under 6): 
   - Input: Name = `Ali`, Age = `5`, Day = `weekday`, Student = `no`  
   - Result: `Ali: 0.00 TRY (Free)`
2. Boundary Age Test (Age 12 limit for Child):  
   - Input: Name = `Ece`, Age = `12`, Day = `weekend`, Student = `yes`  
   - Result: `Ece: 150.00 TRY (Child)`
3. Student Discount Test:  
   - Input: Name = `Can`, Age = `22`, Day = `weekday`, Student = `yes`  
   - Result: `Can: 140.00 TRY (Student)`
   
Why does the order of the rules matter?
The order matters because Python evaluates conditions sequentially from top to bottom and only executes the first rule that matches. If the Student rule came before the Child rule, a 10-year-old student would trigger the Student rule first and receive a 30% discount instead of the 40% Child discount they are entitled to.

# WEEK 04#

AI Tool used: Gemini

Prompt Used: Asked the AI to add error handling('try-except'), range limits (1-100)

What did you change?: Added crash protection for text inputs, blocked numbers outside 1-100 without losing attempts, and styled the square root hint.

Tests:
WELCOME TO THE NUMBER GUESSING GAME!
I picked a number between 1 and 100. You have 7 attemps.!

What is your guess? (Remaining attempts: 7) 105
Invalid number! please enter a number between 1 and 100.
What is your guess? (Remaining attempts: 7) 100
Guess a LOWER number!
What is your guess? (Remaining attempts: 6) 90
Guess a LOWER number!
What is your guess? (Remaining attempts: 5) 80
Guess a LOWER number!
What is your guess? (Remaining attempts: 4) 40
Guess a LOWER number!
What is your guess? (Remaining attempts: 3) 10
Guess a LOWER number!

 HINT: The square root of the secret number is about 1.73!
What is your guess? (Remaining attempts: 2) 3
CONGRATULATIONS! You guessed the number 3 correctly!

Why does the order of the rules matter?: Error and range checks must run first to prevent crashes and invalid inputs before any guess is evaluated or attempts are reduced.

