#! python3
# fillGaps.py - This program finds all files with a given prefix and locates
# any gaps in the numbering (Example: spam001.txt spam002.txt spam004.txt)
# and renames all later files to close this gap.

import os
import re

print('Enter the file prefix you\'d like to sort: ', end='')
filePrefix = input()
searchDir = os.path.join('.', 'spam')
fileRegex = re.compile('^' + filePrefix + r'([0-9]{3})')

num = 1
for dirname, foldernames, filenames in os.walk(searchDir):
    for filename in filenames:
        if result := fileRegex.search(filename):
            if result.group(1) != str(num).zfill(3):
                splitTup = os.path.splitext(filename)
                fileExtension = splitTup[1]
                os.rename(os.path.join(searchDir, filename),
                          os.path.join(searchDir, filePrefix + str(num).zfill(3) + fileExtension))
            num = num + 1
