myPets = ['Zophie', 'Pooka', 'Fat-tail']
name = input('Enter a pet name from '+ str(myPets) + ' : ')
if name not in myPets:
    print('I do not have your pet named: '+ name)
elif name in myPets:
    print(name + ' is my pet')



