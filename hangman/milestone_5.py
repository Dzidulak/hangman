import random 

class Hangman:
    '''
    This class is used to setup a hangman game or the user to play

    Attributes:
        word_list(list): A list of words that the "Computer" will use to randomly pick for user to play.
        num_lives(int): The number of lives the user has when guessing letters.
    '''
    def __init__(self, word_list, num_lives = 5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word =  random.choice(word_list) #Random chosen word by the "computer".
        self.num_letters = len(self.word) #The number of UNIQUE letters in the word that have not been guessed yet 
        self.word_guessed = ['_']*self.num_letters #A list of the letters of the word, with _ for each letter not yet guessed. 
        self.num_lives = num_lives 
        self.word_list = word_list 
        self.list_of_guesses = [] #A list of the guesses that have already been tried.

    def __get_duplicate_letters(self, word, letter):
        '''
        This function is used to find all the indexs of a letter that occurs in a word being guessd.
        Mainly used for find duplicates.

        Args:
            word(str): Word where idex of letter is to be found 
            letter(str): Letter whose index is to be found in the word.

        Returns:
            list: list the indexs of the letter.
        '''
        start_at = -1
        indexs = []
        while True:
            try:
                idx = word.index(letter, start_at+1) #finds index in word starting from a certain index.
            except ValueError:
                break
            else:
                indexs.append(idx)
                start_at = idx #change start index 
        return indexs

    def __update_word_guessed(self, guess):
        '''
        This function updates the word_guessed variable with the correctly guessed letter
        and returns the nu,ber of times that letter occurs in the word.

        Args:
            guess(str): letter user guessed
        
        Returns:
            int: number of spaces replaced 
        '''
        for letter in self.word:
                if guess == letter:
                    indexs = self.__get_duplicate_letters(self.word, letter)#indexs of letter are found
                    for i in indexs:
                        self.word_guessed[i] = guess #each '_' is replcaed with letter guessed 
        return len(indexs)

    def __check_guess(self, guess):
        '''
        This function checks if the users guess is in the word
        God message is printed to user and word_guessed is updated if correct 
        But 1 life is lost and message telling user how many lives are left if incorrect

        Args:
            guess(str): letter user guessed
        '''
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            num_updated_letters = self.__update_word_guessed(guess) #update the word_guessed and get number letters to d
            self.num_letters -= num_updated_letters
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This function callects the users guessed and makes sure it's in the correct format 
        before processing the guess.
        '''
        while True:
            print(self.word_guessed)
            guess = input("\nPlease enter a letter: ")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("\n You Lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("\nCongratulations!! You won the game!")
            break


word_list = ["mango","strawberry","papaya","apple","banana"]
play_game(word_list)


