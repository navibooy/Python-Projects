from art import logo, vs
from game_data import data
import random
from replit import clear
def create_new_option(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

#Show logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  
  #Show 2 options: each has name, description
  print(f"Compare A: {create_new_option(account_a)}.")
  print(vs)
  print(f"Against B: {create_new_option(account_b)}.")
  #The player chooses from the 2 options if Higher or Lower
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  #If the player answered correctly - Update option A to option B and show a new option to compare
  #If the player answered incorrectly - End the Game
  is_correct = check_answer(choice, a_follower_count, b_follower_count)
  
  clear()
  print(logo)
  #Show the current score
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
  
  
  
 
  

  
  