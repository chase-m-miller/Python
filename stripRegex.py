#! python3
# this program implements the strip() function using regex

import re


def regexStrip(text, opt=None):
    if opt == 'start':
        # remove whitespace from beginning of string
        text = re.sub(r'^\s+', '', text)
        print(text)
        return
    elif opt == 'end':
        # remove whitespace from end of string
        text = re.sub(r'\s+$', '', text)
        print(text)
        return
    else:
        text = re.sub(r'^\s+', '', text)
        text = re.sub(r'\s+$', '', text)
        print(text)
        return


regexStrip('   Does this work?   ')
regexStrip('\t\t\tHow about this?\t\t\t')
regexStrip('   Just the start?   ', opt='start')
regexStrip('   Just the end?   ', opt='end')
