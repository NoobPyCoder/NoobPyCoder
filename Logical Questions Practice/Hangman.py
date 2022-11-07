import random
from words import words
import string

def guessed_word(words):
    # randomly chooses something from the words list and give a single word to user to guess
    word = random.choice(words)
    # it will help computer to choose a word without '-' or with any white spaces
    while '-' in word or ' ' in word:
        word = random.choice(words)
    # this will help the chosen word to be in Upper case format
    return word.upper()

# this function will help us to remember which alphabets we have guessed and 
# keep track of the filled letters in word
def hangman():
    # Firstly, get the randomly guessed woord
    word = guessed_word(words)
    word_letters = set(word)  # saves letters in the word, keeping track of waht already have been guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # empty set to track what the user has guessed

    # this will ensure to run the loop till all the letter in the word are not guessed
    while len(word_letters) > 0:
        #this will show user which letters they have used    
        print('You have already used this letter.', ' '.join(used_letters))
        #this will show user which letters they have guessed correctly and '- and space as a replacement
        # of the letter they haven't guessed yet
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))
        # getting user input and setting it in the words
        user_letter = input("Guess a letter: ").upper()
        # this will help us to add the letters which is a valid alphabet to used_letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # if the letter that user guessed is in the word, it will remove it from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        # this will infomr user that they have already guessed this letter
        elif user_letter in used_letters:
            print('You have already guessed this letter, Please Try Again.')

        else:
            print('Invalid Character. Please Try Again.')
    
    else:
        print('YAY! You guessed the word', word, '!!')

hangman()
