import math
import random
secret_number = random.randint(1, 100)
attempts = 7
print("WELCOME TO THE NUMBER GUESSING GAME!") 
print("I picked a number between 1 and 100. You have 7 attemps.!\n")
while attempts > 0:
  try:
    guess = int(input(f"What is your guess? (Remaining attempts: {attempts}) "))
  except ValueError:
    print("Please enter a valid whole number! (letters or empty inputs are not allowed)")
    continue
  if guess < 1 or guess > 100:
    print("Invalid number! please enter a number between 1 and 100." )
    continue
  if guess == secret_number:
    print(f"CONGRATULATIONS! You guessed the number {secret_number} correctly!")
    break
  elif guess < secret_number:
    print("Guess a HIGHER number!")
  else:
    print("Guess a LOWER number!") 
  attempts -= 1
  if attempts == 2:
    square_root = math.sqrt(secret_number)
    print(f"\n HINT: The square root of the secret number is about {square_root:.2f} ")
if attempts == 0:
  print(f"\n Unfotunately, you ran out of attempts! The number was: {secret_number}.")
