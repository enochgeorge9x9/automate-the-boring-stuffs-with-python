#Comma Code
'''
#my try -- comma code
import copy
def commacode(item_list):
    a= copy.copy(item_list)
    print('Items are : ', end = '')
    for i in range(len(a)-1):
        print(', '.join(a[0:-1]), end = '')
        break
    print(' and ' + a[-1])

spam = ['apples', 'bananas', 'tofu', 'cats', 'maslkgj', 'sihf']
commacode(spam)
'''
'''
#internet solution for Comma Code
def commacode(item_list):
    if len(item_list) == 1:
        return item_list[0]
    return '{} , and {}'.format(', '.join(item_list[:-1]), item_list[-1])


spam = ['apples', 'bananas', 'tofu', 'cats']
m = commacode(spam)
print(m)

'''

#Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['.', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.']]

'''
rows = len(grid) #number of elements in the gird list
cols = len(grid[0])#number of elements in each column of the the list

for i in range(cols):
    for j in range(rows):
        print(grid[j][i], end = '')
    print()
'''

#simpler method
print('\n'.join(map(''.join, zip(*grid))))


