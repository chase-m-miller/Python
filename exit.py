import sys

while True:
    print('Enter exit to exit.')
    answer = input()
    if answer == 'exit':
        sys.exit()
    print('You entered: ' + answer)
