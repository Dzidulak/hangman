import random 
import string 

word_list = ["mango","strawberry","papaya","apple","banana"]
alphabet = list(string.ascii_letters) # list of the alpahbet in uppercase and lowercase.

word = random.choice(word_list)
print(word)

guess = input("Please enter a letter: ")

if len(guess) == 1 and guess in alphabet:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")