import os

# This will delete all .txt files in the cwd
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename)
