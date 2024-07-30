#! python3

import os

# TODO: Open and read text file
madlibFile = open(r'madlib.txt', 'r')
madlibStr = madlibFile.read().split()

# TODO: Scan for ADJECTIVE, NOUN, VERB, and ADVERB
for word in madlibStr:
    print(word)
    if word == 'ADJECTIVE':
        print('Enter an adjective: ', end='')
        adjective = input()
        word.replace(word, adjective)
    elif word == 'NOUN':
        print('Enter a noun: ', end='')
        noun = input()
        word.replace(word, noun)
    elif word == 'VERB':
        print('Enter a verb: ', end='')
        verb = input()
        word.replace(word, verb)
    elif word == 'ADVERB':
        print('Enter an adverb: ', end='')
        adverb = input()
        word.replace(word, adverb)

# TODO: Prompt the user to replace any occurences

# TODO: Create a new text file, print new string and write to file

madlibFile.close()
