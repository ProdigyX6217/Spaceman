# Helped by Audi
import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # True if letter guessed == Secret Word, False otherwise
    for letter in secret_word:
        if letter != letters_guessed:
            return False

    return True
#TODO: Show guessed letter (so far)
def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, show an _ (underscore) instead.
    '''
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    string = ""

    for letter in secret_word:
        if letter in letters_guessed:
            string += letter
        else:
            string += "_"
    print (string)
    return string

#TODO: Check if guessed letter is in/not in secret_word
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if guess in secret_word:
        return True
    else:
        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    remaining_guesses = len(secret_word)
    letters_guessed = []
#TODO: Ask player to guess 1 letter/round and check if only 1 letter
    running = True
    while running:
        guessing = True
        while guessing:
            guess = input("Guess A Letter: ")
            if guess.isalpha() and len(guess) == 1:
                letters_guessed.append(guess)
                guessing = False
            else:
                print("Incorrect Input")
#TODO: Show game information based on project spec
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if is_guess_in_word(guess, secret_word):
             print("Correct Guess")
        else:
            print("Incorrect Guess")
            remaining_guesses -= 1
            print("Guesses Left: " + str(remaining_guesses))

        print(guessed_word)
#TODO: Check if game has been Won/Lost
        if is_word_guessed(secret_word, letters_guessed):
            print("Game Won")
            running = False
        elif remaining_guesses == 0:
            print("Game Lost " + secret_word)
            running = False














#These function calls that will start the game
running = True
while running:
    secret_word = load_word()
    spaceman(secret_word)
    new_game = input("Play Again? (Y/N) ")
    if "N" == new_game:
        running = False
