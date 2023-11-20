import random 
import string


def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a letter: ")

        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print( "Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

word_list = ["mango","strawberry","papaya","apple","banana"]
word = random.choice(word_list) #Random chosen word by the "computer".

alphabet = list(string.ascii_letters) # list of the alpahbet in uppercase and lowercase.

ask_for_input()
