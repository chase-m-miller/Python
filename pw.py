#! python3
# This is a simple password manager.
import sys
import pyperclip

PASSWORDS = {'email': 'placeholderpassword123',
             'blog': 'fakepassword12',
             'luggage': '54321'}

if len(sys.argv) > 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
