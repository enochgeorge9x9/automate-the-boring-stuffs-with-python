#using while loop with continue
while True:
    name = input('What is your Name: ')
    if name != 'Joe':
        continue
    password= input('Hello Joe. What is your Password? (hint its a fish): ')

    if password == 'swordfish':
        break
print ('Access Granted')
