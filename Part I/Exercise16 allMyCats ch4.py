#allmMyCat example through list
##catNames = []
##while True:
##    print('Enter the name of the cat ' + str(len(catNames)+1)+ ': ', end = '')
##    name = input()
##    if name == '':
##        break
##    catNames = catNames + [name]
##
##print('The cat names are: ', end='')
##for name in catNames:
##    print(' ' + name,  end=',')



#sample test
a=['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(a)):
    print('Index' + str(i)  + ' in supplies is: ' + a[i])
    
print('pens' in a) # to check if there is anything in the list

