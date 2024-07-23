#! python3
# strongPassword.py - detects if password is strong enough
import re

capRegex = re.compile(r'[A-Z]+')
lowRegex = re.compile(r'[a-z]+')
numRegex = re.compile(r'\d+')
lenRegex = re.compile(r'(\w|\d){8,}')

print('Enter a password to test: ', end='')
password = input()
if (capRegex.search(password) and lowRegex.search(password) and 
   numRegex.search(password) and lenRegex.match(password)):
    print('Your password is strong enough.')
else:
    print('Your password is weak.')
    print('''Make sure your password contains upper and lowercase letters,
at least one number, and is at least 8 characters long.''')
