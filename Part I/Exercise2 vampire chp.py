#if elif and else statements or flow control exercise 
name = input('What is your name: ')
age = input('What is your age: ')

if name == 'Alice':
    print('Hi, Alice')
elif int(age)<12:
    print('You are not Alice,kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) >100:
    print('You are not Alice,grannie.')
