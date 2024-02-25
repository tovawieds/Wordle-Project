
#######################################################
# wordle_engine
#########################################################


# Container for color control codes.
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"

def welcome_string():
    return f"Welcome to {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r{wordle_colors.YELLOW}d{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"

def create_letter_status():
    """ Initialize and Return a new dictionary that maps each letter to
        wordle_colors.BLUE """
    # dictionary that will have the words
    alpha = {}
    # loop through the letters and add each to dictionary, mapping to the color blue
    for letter in wordle_alphabet:
        alpha[letter] = wordle_colors.BLUE
    # return the new dictionary
    return alpha

def load_words(filename: str):
    """ Load the words from the specified file and place them
        in a set.
        Ignore any lines that begin with "#"
        """
    # create a set to load the words into
    words_set = set()
    # open the file, if the line doesn't start with '#', add the word to the set
    with open(filename) as file:
        for line in file:
            if line[0] != "#":
                words_set.add(line)
    # return the set of words
    return words_set

def format_guess(target, guess):
    """ Return a string that contains the user's guess formatted
        so that each letter is colored
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word,
                  but in a different location.
        * RED:    The letter does not appear in the target word
        Also, the string should end with wordle_colors.ENDC """
    new_word = ""
    for letter in guess:
        if letter in new_word:
            try:
                new_target = target[(target.index(letter)):]
                new_guess = guess[(guess.index(letter)):]
                if letter in new_target:
                    if new_guess.index(letter) == new_target.index(letter):
                        new_word += f"{wordle_colors.GREEN}{letter}{wordle_colors.ENDC}"
                    else:
                        new_word += f"{wordle_colors.YELLOW}{letter}{wordle_colors.ENDC}"
                else:
                    new_word += f"{wordle_colors.RED}{letter}{wordle_colors.ENDC}"
            except ValueError:
                new_word += f"{wordle_colors.RED}{letter}{wordle_colors.ENDC}"
        elif letter in target:
            if guess.index(letter) == target.index(letter):
                new_word += f"{wordle_colors.GREEN}{letter}{wordle_colors.ENDC}"
            else:
                new_word += f"{wordle_colors.YELLOW}{letter}{wordle_colors.ENDC}"
        else:
            new_word += f"{wordle_colors.RED}{letter}{wordle_colors.ENDC}"
    return new_word

def update_letter_status(letter_status, target, guess):
    """ Update the letter status dictionary to show which letters
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""
    # loop through each letter in guess
    for letter in guess:
        # if the letter appears in the targeted word, check ehere it is
        if letter in target:
            # if the letter is in the right spot, ake it green
            if guess.index(letter) == target.index(letter):
                letter_status[letter] = wordle_colors.GREEN
            # if the letter is in the wrong spot, make it yellow
            else:
                letter_status[letter] = wordle_colors.YELLOW
        # if the letter does not appear at all, make it red
        else:
            letter_status[letter] = wordle_colors.RED

def format_letters(alphabet_dict):
    """ Generate a string that lists all the letters of the alphabet
        colored according to the rules given in update_letter_status.
        the string should end with wordle_colors.ENDC """
    new_alpha = ""  # variable for teh new alphabet letters
    # add the letter in the right color to the alphabet
    for letter in alphabet_dict:
        new_alpha += alphabet_dict[letter] + letter
    return new_alpha + wordle_colors.ENDC  # return the new alphabet





# letters = create_letter_status()
# print(letters)
# update_letter_status(letters, "hello", "steak")
# for letter in letters:
#     print(letters[letter] + letter)
# print('\033[94m' + "a")
