# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    """# my 1st code
    #wordGuessed = ""
   # for n in secretWord:
    	# if n in lettersGuessed:
    	#	wordGuessed += n
    #   return bool(len(secretWord) == len(wordGuessed))"""
    set(secretWord) <= set(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return "".join([e if e in lettersGuessed else "_" for e in secretWord])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return "".join(sorted(b for b in set("abcdefghijklmnopqrstuvwxyz") if b not in set(lettersGuessed)))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    secretWord = secretWord
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    def guessesLeft(num):
        print("You have " + str(num) + " guesses left")

    def getGuessedWord(secretWord, lettersGuessed):
        '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
        # FILL IN YOUR CODE HERE...
        return "".join([e if e in lettersGuessed else "_" for e in secretWord])

    num = 8
    lettersGuessed = ""

    while set(secretWord) not in set(lettersGuessed):
        print("-------------")
        if set(secretWord) <= set(lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
        guessesLeft(num)
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters: " + availableLetters)
        raw_guess = input("Please guess a letter: ")
        guess = raw_guess.lower()
        if num <= 1:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        if guess in availableLetters and guess in secretWord:
            lettersGuessed += (guess * secretWord.count(guess))
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            num = num
            print(lettersGuessed)
        elif guess in availableLetters and guess not in secretWord:
            lettersGuessed += guess
            print("Oops! That letter is not in my word:" + getGuessedWord(secretWord, lettersGuessed))
            num -= 1
        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            num = num

    if num <= 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

hangman(chooseWord(wordlist))
