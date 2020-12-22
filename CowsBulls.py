import random
"""
CowsBulls.py

Emulates the game "Cows and Bulls" or "Mastermind"
User guesses a set of numbers (4 by default) and the computer lets you know how many are correct, and how
many are in the correct position

"""

NumberOfDigits = 4 #size of the game
board = [] #board that contains the answers


def getGuess():
    '''Requests the user for an integer (their guess).  If anything except an integer is entered,
    it returns the string "0"


    Returns: string (of numbers)
    '''
    try:
        retrieved_guess = int(input("Guess:"))
        guess = str(retrieved_guess)
    except ValueError:
        retrieved_guess = 0
        guess = str(retrieved_guess)
        
    return guess
    

#Create the random numbers
count = NumberOfDigits
while count > 0:

    board.append(random.randint(0,9))
    count -= 1


def split(word):
    '''Converts the string of integers into an array of integers for comparing.

    Keyword arguments:
    word -- String of integers

    Returns: list of integers (of size NumberOfDigits)
    '''

    listOfInts = [char for char in word]
    listOfInts = [int(i) for i in listOfInts]
        
    return listOfInts
    
def findBulls(guessInts, varBoard):
    '''increments bulls when a guess integer is found in the board (avoids repeats)

    Keyword arguments:
    guessInts -- String of integers the user input
    varBoard -- a copy of the full answers that can be edited in order to avoid repeats

    Returns: int - number of "Bulls"
    '''

    retBulls = 0
    for item in guessInts:
        if item in varBoard:
            varBoard.remove(item)
            retBulls += 1
    
    return retBulls
    
def upgradeBulls(guessInts, varBoard):
    '''Counts the number of times both the number and positions of the guess match that of the board.

    Keyword arguments:
    guessInts -- String of integers the user input
    varBoard -- a copy of the full answers that can be edited in order to avoid repeats

    Returns: int - number of "Cows"
    '''

    numCows = 0
    count = 0
    while count < NumberOfDigits:
        if guessInts[count] == varBoard[count]:
            numCows += 1
        count += 1
        
    return numCows
       
def CountCowBulls(guess):
    '''Counts the number of bulls, then cows while adjusting bulls.

    Keyword arguments:
    guess -- String of integers the user input

    Returns: info - array with both number of bulls and cows
    '''
    guessVar = split(guess)
    variableBoard = board.copy()
    
    bulls = findBulls(guessVar, variableBoard)
    variableBoard = board.copy()
    cows = upgradeBulls(guessVar, variableBoard)
    bulls = bulls - cows
    
    
    print(guessVar)
    print('Bulls: ' + str(bulls))
    print('cows: ' + str(cows))
    
    info = [bulls, cows]
    return info


#game loop starts here
bulls, cows, turnCount = [0,0,0]
while cows != NumberOfDigits:


    bulls, cows = [0,0]
    guess = getGuess()
    if NumberOfDigits > len(guess):
        
        count = NumberOfDigits - len(guess)
        while count > 0:
            guess = "0" + guess
            count -= 1
        print(guess)
        bulls, cows = CountCowBulls(guess)

    elif len(guess) > NumberOfDigits:
        print("guess too many digits")
        
    else:
        print(guess)
        bulls, cows = CountCowBulls(guess)
     
    turnCount += 1
        
print("you got it with " + guess + ' using ' + str(turnCount) + ' turns. ')

