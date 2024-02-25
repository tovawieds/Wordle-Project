
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
    target = random.choice(list(valid_words))  # <== change this
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

all_letters = wordle_engine.create_letter_status()
for i in range(5):
    guess = input(f"Make a guess ({wordle_engine.format_letters(all_letters)}): ")
