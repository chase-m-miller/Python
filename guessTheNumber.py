import random
answer = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesMade in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < answer:
        print('Too low!')
        continue
    elif guess > answer:
        print ('Too high!')
        continue
    else:
        print('Good job! You guessed my number in ' + str(guessesMade) + ' guesses!')
        exit()

print('You\'re out of guesses. The correct answer was ' + str(answer) + '. You lose!')
