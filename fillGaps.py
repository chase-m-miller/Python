#! python3
# fillGaps.py - This program finds all files with a given prefix and locates
# any gaps in the numbering (Example: spam001.txt spam002.txt spam004.txt)
# and renames all later files to close this gap.

import os
import re

searchDir = os.path.join('.', 'spam')
filePrefix = re.compile(r'^spam([0-9]{3})')

for dirname, foldernames, filenames in os.walk(searchDir):
    for filename in filenames:
        if filePrefix.match(filename):
            print(filename)
