#Step 5

import random
import hangman_words
import hangman_art
from replit import clear
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

print(hangman_art.logo)
print("Welcome to the hangman game. You only have 7 tries to guess a letter and complete the word. Goodluck!\n")
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 7

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Create blanks
display = []
chosen_letters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    chosen_letters.append(guess)
    clear()
    if guess in display:
      print(f"You've already guessed letter {guess}. Try again.")
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You've guessed {guess}, that is not part of the word. ")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word is {chosen_word}.")
            
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n\n You have already tried these letters: ")
    print(chosen_letters)

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages = hangman_art.stages
    print(stages[lives])
