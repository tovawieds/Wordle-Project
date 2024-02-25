
#######################################################
# wordle
#########################################################

# This is the "main" portion of your game.
# Any code that uses stdin or stdout (i.e., input() and print())
# should go in this file.

import wordle_engine
import random
import sys


# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")

# Use the target word provided on the command line,
# or, choose a random word if no target word given.
if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    # TODO choose a random word from valid_words
    used_words = wordle_engine.load_words("shuffled_real_wordles.txt")
    target = random.choice(list(used_words))  # <== change this
#########
# # choose a word at random from the list of words
# used_words = wordle_engine.load_words("shuffled_real_wordlist.txt")
# target = random.choice(used_words)
#########

# TODO Implement the rest of the game.
# Remember:
#   * Guesses must be exactly 5 letters
#   * Guesses must be valid words
#   * Players get at most 6 guesses
#   * Please display the entire history of guesses before each prompt.
#   * Print a message at the end of the game indicating whether the player won or lost.
#      * If the player wins, display the entire sequence of guesses as part of the final message.

guessed_words = []  # list of the user's guesses
# function to add the user's guess to the list of guesses
def add_guess(guess):
    word = wordle_engine.format_guess(target, guess)
    guessed_words.append(f"{i + 1}. {word}")

# function to deternime if the user won
def did_win(guess):
    if guess == target:
        return True
    return False

all_letters = wordle_engine.create_letter_status()  # the alphabet formattted into colors
win = False  # variable to know if the user won
# loop to ask the user to guess, up tp 6 times
i = 0
while i < 5:
    for word in guessed_words:
        print(word)
    guess = input(f"Make a guess ({wordle_engine.format_letters(all_letters)}): ")
    if (guess + "\n") not in valid_words or len(guess) != 5:
        print("Not a valid word")
    else:
        add_guess(guess)
        if did_win(guess):
            for word in guessed_words:
                print(word)
            print("You win!")
            win = True
            break
        i += 1
        wordle_engine.update_letter_status(all_letters, target, guess)
if not win:
    print("You loose:( the word was: " + target)
