import random

message = ['It is certain', 'It is decidedly so', 'Yes Definitely!', "Reply hazy try again", 'Ask again later',
           'Concentrate and ask again', 'My Reply is no', 'Outlook not so good', 'very doubtful']

print(message[random.randint(0, len(message) -1)])
print(len(message)-1)


