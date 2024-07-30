#! python3

import re

noun = re.compile('NOUN')
verb = re.compile('VERB')
adjective = re.compile('ADJECTIVE')
adverb = re.compile('ADVERB')

# Open and read text file
madlibFile = open('madlib.txt', 'r')
madlibStr = madlibFile.read().split()

# Scan for ADJECTIVE, NOUN, VERB, and ADVERB
index = 0
for word in madlibStr:
    print(word)
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

newString = ' '.join(madlibStr)
print(newString)
# TODO: Prompt the user to replace any occurences

# TODO: Create a new text file, print new string and write to file

madlibFile.close()
