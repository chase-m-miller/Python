import random


def tossCoin():
    num = random.randint(0, 1)
    if num == 0:
        return 'tails'
    else:
        return 'heads'


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
    toss = tossCoin()  # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        toss = tossCoin()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
