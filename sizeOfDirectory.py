#! python3
# this script gets the size of the current working directory
import os

totalSize = 0
for filename in os.listdir('.'):
    totalSize += os.path.getsize(os.path.join('.', filename))

print(str(totalSize) + ' bytes')
