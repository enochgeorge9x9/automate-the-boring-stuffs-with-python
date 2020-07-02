#! python3
#pw.py - An insecure password locker program
filename = 'Exercise28 pwProject ch6.py'

PASSWORDS = {'email' : ' Encohohcedlsjlsjaohoijsfd',
                         'blog' : ' slksjfodjsoifjfjwejoiefjewlf',
                         'luggage' : '6172'}

import pyperclip 
import sys
if len(sys.argv) < 2:
    print('Usage: python '+ filename +' [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account +' copied to clipboard.')
else:
    print('There is no account named' + account)


    
