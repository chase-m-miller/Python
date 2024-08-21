#! python3
# findLargeFiles.py - This program walks the cwd looking for files that are
# above a specified file size and prints their location to the screen.

import os

searchDir = os.path.abspath('.')

for dirpath, dirnames, filenames in os.walk(searchDir):
    print(dirpath + ':')

    for dirname in dirnames:
        print('SUBFOLDER: ' + dirname)

    for filename in filenames:
        print('FILENAME: ' + filename)
