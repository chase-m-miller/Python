#! python3
# regexSearch.py - This program opens all .txt files in a folder
# and searches for any line that matches a user-supplied
# regular expression. The result is printed to the screen.

import re
import os

# Get regular expression from user.
print('Enter a regular expression: ', end='')
userInput = input()
userRegex = re.compile(userInput)


# TODO: Search cwd for .txt files and open all of them.
for filename in os.listdir('.'):
    file = os.path.join('.', filename)
    if os.path.isfile(file):
        openedFile = open(file, 'r')
        fileContents = openedFile.read()
        if userRegex.search(fileContents):
            print(filename)
            print('-------------------------')
            print(fileContents)
        openedFile.close()
