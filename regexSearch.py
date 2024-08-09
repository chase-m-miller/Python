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

# Search cwd for files and open all of them.
# Search the contents of the files for a regex match,
# and print the file if a match is found.
for filename in os.listdir('.'):
    filePath = os.path.join('.', filename)
    if os.path.isfile(filePath):
        openedFile = open(filePath, 'r')
        fileContents = openedFile.read()
        if userRegex.search(fileContents):
            print(filename)
            print('-------------------------')
            print(fileContents)
        openedFile.close()
