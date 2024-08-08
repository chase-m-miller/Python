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
    if os.path.isfile(file) and userRegex.search(file):
        openedFile = open(file, 'r')
        fileContents = openedFile.read()
        if userRegex.search(fileContents):
            print(filename)
            print('____________________________')
            print(fileContents)
        # print(openedFile.read())
        openedFile.close()

# TODO: Search the .txt files for lines matching regex
#       and print them to the screen.

# TODO: Close all of the opened .txt files.
