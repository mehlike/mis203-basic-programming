#Week03 lab: order approval policy
test table
unit price / stock / quantity / member / result

100        / 10     / 0       / yes    / rejected: invalid quantity

100        / 5      / 10      / no     / rejected: insufficient stock

100        / 10     / 5       / yes    / approved: discount applied (450.00) 


Notes:
I tested 500 TRY with a member user to see if the 10% discount works correctly.
I added '.lower()' to the member input so the code works even if the user types 'YES' or 'Yes'.
