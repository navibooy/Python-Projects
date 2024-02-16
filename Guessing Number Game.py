

import random
from art import logo

life = 0
#Choose a random number between 1 and 100.
number = random.randint(0,100)

def decrease_lives():
  """Decrease the life every guess"""
  return life - 1
  
def calculate_score(user_guess):
  """Calculate the score and print the message"""
  if user_guess > number:
    print("Too high. Guess again.")
  elif user_guess < number:
    print("Too low. Guess again.")
  else:
    print(f"You got it! The answer was {number}.👏👏")
    

#Print the welcome message and choose the difficulty
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
option = input("Choose a difficulty. Type 'easy' or 'hard': ")

#Set the lives depending on the difficulty
if option == 'easy':
  life += 10 
else:
  life += 5

game_over = False
guess = 0
while not game_over:
  print(f"You have {life} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  calculate_score(guess)
  life = decrease_lives()
  if number == guess:
    game_over = True
  elif life == 0:
    print(f"You've run out of guesses, the answer is {number} you lose. 😜")
    game_over = True
  
    


