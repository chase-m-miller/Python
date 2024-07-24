#! python3
# this program implements the strip() function using regex

import re


def regexStrip(text):
    # remove whitespace from beginning of string
    text = re.sub(r'^\s+', '', text)
    # remove whitespace from end of string
    text = re.sub(r'\s+$', '', text)
    print(text)


regexStrip('   Does this work?   ')
regexStrip('\t\t\tHow about this?\t\t\t')
