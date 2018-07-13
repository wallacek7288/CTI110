#Secret Number Guessing Game
#July 8, 2018
#CTI-110 P5HW2 - Random Number Guessing Game
#Kaiya Hall
#


import random

MAX = 100
MIN = 1

secretNumber = random.randint(1,MAX)

MaxGuess = 10
guesses_left = MaxGuess

def main():

    print('Guess a number between 1 and 100!')

    again = 'y'

    while again == 'y' or again == 'Y' :
        
        guess = int(input('Enter your guess : '))
        if guess == secretNumber:
            print('Youre Correct, great guess!')
            again = input(' Want to play again? (y = yes): ')
        elif guess < secretNumber:
           print('Try again, thats too low')
        else:
            print('Try again, Thats too high')
        
    
    
        

main()
               

