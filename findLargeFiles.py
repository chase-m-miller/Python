#! python3
# findLargeFiles.py - This program walks the cwd looking for files that are
# above a specified file size and prints their location to the screen.

import os

minFileSize = 8000  # Files above this size (in bytes) will be printed
searchDir = os.path.abspath('.')

for dirpath, dirnames, filenames in os.walk(searchDir):
    for filename in filenames:
        filePath = os.path.join(dirpath, filename)
        if os.path.getsize(filePath) > minFileSize:
            print(filePath + ' exceeds ' + str(minFileSize) + ' bytes.')
