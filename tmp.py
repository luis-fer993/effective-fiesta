#hangman.py

import random ,sys,os

HANGMANPICS=[''' 
             
     +---+
     |   |
         |    
         |    
         |   
         |    
 ============''',
 ''' 
             
     +---+
     |   |
     0   |    
         |    
         |   
         |    
 ============''',
 ''' 
             
     +---+
     |   |
     0   |    
     |   |    
         |   
         |    
 ============''',
 ''' 
             
     +---+
     |   |
     0   |    
    /|   |    
         |   
         |    
 ============'''
 ,
 ''' 
             
     +---+
     |   |
     0   |    
    /|\  |    
         |   
         |    
 ============''' ,
 ''' 
             
     +---+
     |   |
     0   |    
    /|\  |    
    /    |   
         |    
 ============''',
 ''' 
             
     +---+
     |   |
     0   |    
    /|\  |    
    / \  |   
         |    
 ============'''
 ]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRamdomWord(wordList):
    wordIndex=random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    os.system('cls')
    print(HANGMANPICS[len(missedLetters)],end='\n')
    print('Missedletters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks='_'*len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
    
    for letter in blanks:
        print(letter, end='')
    print()
    
    
def getGuess(alredyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        guess=input('Guess a letter.').lower()
        if len(guess)!=1:
            print('Please enter asingle letter.')
        elif guess in alredyGuessed:
            print("You've already guessed that letter.Choose again.")
        elif guess not in  'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    return input('Do you wnat to play again? (yes or no)').lower().startswith('y')

print('HANGMAN')
missedLetters=''
correctLetters=''
secretWord=getRamdomWord(words)
GameIsDone=False

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess=getGuess(missedLetters+correctLetters)
    
    if guess in secretWord:
        correctLetters+=guess
        
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i]not in correctLetters:
                foundAllLetters=False
                break
        
        if foundAllLetters:
            print('YES, The secret Word is %s, You have won!!'%(secretWord))
            GameIsDone=True
    else:
        missedLetters+=guess
        
        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"') 
            
            GameIsDone=True
        
        if GameIsDone:
            if playAgain():
                missedLetters=''
                correctLetters=''
                secretWord=getRamdomWord(words)
                GameIsDone=False
            else:
                break