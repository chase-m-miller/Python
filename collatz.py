def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter a number.')
while True:
    try:
        userInput = int(input())
        break
    except ValueError:
        print('You must enter an integer.')

result = collatz(userInput)
while True:
    if result == 1:
        break
    else:
        result = collatz(result)
        print(result)
