import pprint #pretty print


#without using pretty print
'''
message = 'It was a bright cold day in April, and the clocks were striking thirteen. '
count = {}

for character in message:
    count.setdefault(character, 0 )
    count[character] = count[character]+1


print(sorted(count.items()))
'''

#with using pretty print
message = 'It was a bright cold day in April, and the clocks were striking thirteen. '
count = {}

for character in message:
    count.setdefault(character, 0 )
    count[character] = count[character]+1

pprint.pprint(sorted(count.items()))


