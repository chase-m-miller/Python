#! python3
# madlib.py - This program looks in the current directory for a file
# named 'madlib.txt', and prompts the user to replace any occurences
# of NOUN, VERB, ADJECTIVE, or ADVERB. The program then prints the
# new string, writes it to 'madlib_filled.txt', and terminates.

import re

# Regex used for substitutions
noun = re.compile('NOUN')
verb = re.compile('VERB')
adjective = re.compile('ADJECTIVE')
adverb = re.compile('ADVERB')

# Open and read text file, then split it into a list
madlibFile = open('madlib.txt', 'r')
madlibStr = madlibFile.read().split()

# Scan for ADJECTIVE, NOUN, VERB, and ADVERB
# If found, prompt user for replacement
index = 0
for word in madlibStr:
    if adjective.match(word):
        print('Enter an adjective: ', end='')
        userInput = input()
        madlibStr[index] = re.sub(adjective, userInput, word)
    elif noun.match(word):
        print('Enter a noun: ', end='')
        userInput = input()
        madlibStr[index] = re.sub(noun, userInput, word)
    elif verb.match(word):
        print('Enter a verb: ', end='')
        userInput = input()
        madlibStr[index] = re.sub(verb, userInput, word)
    elif adverb.match(word):
        print('Enter an adverb: ', end='')
        userInput = input()
        madlibStr[index] = re.sub(adverb, userInput, word)

    index += 1

# Create a new text file, print new string and write to file
newString = ' '.join(madlibStr)
print(newString)

madlibCompleted = open('madlib_filled.txt', 'w')
madlibCompleted.write(newString)

madlibFile.close()
madlibCompleted.close()
