#! python3
import os

print('Input a directory to walk: ', end='')
searchDir = input()

for folderName, subfolders, filenames in os.walk(searchDir):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')
