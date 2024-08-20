#! python3
# selectiveCopy.py - This program walks through a folder tree and searches for
# a certain file extension (such as .pdf or .jpg). The program then copies
# these files from there current location to a new folder.

import os
import shutil

print('Input a directory to walk: ', end='')
searchDir = input()

print('Input a directory to copy to: ', end='')
copyToDir = input()

for folderName, subfolders, filenames in os.walk(searchDir):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
        if filename.endswith(".pyw"):
            print('Copying to new directory...')
            shutil.copy(os.path.join(folderName, filename), copyToDir)

    print('')
