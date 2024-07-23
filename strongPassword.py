#! python3
# strongPassword.py - detects if password is strong enough
import re

charRegex = re.compile(r'[A-Z]+[a-z]+\d+')
lenRegex = re.compile(r'(\w|\d){8,}')

print('Enter a password to test: ', end='')
password = input()
if (charRegex.search(password) and lenRegex.match(password)):
    print('Your password is strong enough.')
else:
    print('Your password is weak.')
    print('Make sure your password contains upper and lowercase letters,')
    print('at least one number, and is at least 8 characters long.')
