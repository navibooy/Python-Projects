
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from replit import clear
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_num = random.choice(cards)
  return random_num

def calculate_score(list_cards):
  """Take a list of cards and return the total score from the cards"""
  if sum(list_cards) == 21 and len(list_cards) == 2:
    return 0
  if sum(list_cards) > 21 and 11 in list_cards:
    for i in range(len(list_cards)):
      if list_cards[i] == 11:
        list_cards[i] = 1
  return sum(list_cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw! 😧"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack! 😔"
  elif user_score == 0:
    return "Win with a Blackjack! 😋"
  elif computer_score > 21:
    return "Opponent went over, you win! 😍"
  elif user_score > 21:
    return "You went over, you lose! 😭"
  elif user_score > computer_score:
    return "You win! 😇"
  else:
    return "You lose! 🙄"
  


def play_game():

  print(logo)
  computer_cards = []
  user_cards = []
  
    
  
  while len(computer_cards) < 2:
    computer_cards.append(deal_card())
  
  while len(user_cards) < 2:
    user_cards.append(deal_card())
  
  is_game_over = False
  while not is_game_over:
    total_user = calculate_score(user_cards)
    total_computer = calculate_score(computer_cards)
  
    print(f"Your cards: {user_cards}, current score: {total_user}")
    print(f"Computer's first card: {computer_cards[0]}\n")
  
    if total_user == 0 or total_computer == 0 or total_user > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to draw another card, type 'n' to pass: \n")
      if user_should_deal == "y":
          user_cards.append(deal_card())
      else:
          is_game_over = True
  
  
  while total_computer != 0 and total_computer < 17:
    computer_cards.append(deal_card())
    total_computer = calculate_score(computer_cards)
    
  print(f"Your final hand: {user_cards}, final score: {total_user}.")
  print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
  print(compare(total_user, total_computer))
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()