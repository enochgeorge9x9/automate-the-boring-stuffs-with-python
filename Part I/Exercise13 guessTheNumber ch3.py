#this is a guess number game.
import random

    


randomNum = random.randint(1,20)
print('I am thinking the a number from 1 to 20. Guess the Number: ')

for i in range(1,7):
    print ('Take a guess: ', end='')
    guess = int(input())
    if guess < randomNum:
        print('Your guess is too low')
    elif guess > randomNum:
        print('Your guess is too high')
    else:
        break
if guess == randomNum:
    print('Good Job! You guessed my Number in ' + str(i) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(randomNum))


    
