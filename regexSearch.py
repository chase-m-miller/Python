#! python3
# regexSearch.py - This program opens all .txt files in a folder
# and searches for any line that matches a user-supplied
# regular expression. The result is printed to the screen.

import re
import os

# Test input as regex.
testString = 'String to match'
print('Enter a regular expression: ', end='')
userInput = input()
print(userInput)
userRegex = re.compile(userInput)
print(userRegex.search(testString))

# TODO: Get regular expression from user.

# TODO: Search cwd for .txt files and open all of them.
for filename in os.listdir('./'):
    file = os.path.join('./', filename)
    openedFile = open(file, 'r')
    print(openedFile)
    openedFile.close()

# TODO: Search the .txt files for lines matching regex
#       and print them to the screen.

# TODO: Close all of the opened .txt files.
