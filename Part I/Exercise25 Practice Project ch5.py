
#Inventory
'''
inventory = {'rope':1, 'torch':6, 'gold coin': 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
    print('Inventory:' )
    total = 0
    for t,n in inventory.items():
        print(str(n) + ' ' + str(t))
        total += n
    print('Total number of items: ', total)
    
displayInventory(inventory)
'''




#Fantasy Game Inventory
def addToInventory(inventory, addedItem):

    for i in range(len(addedItem)):
        if addedItem[i] in inventory:
            inventory[addedItem[i]] = inventory[addedItem[i]] + 1
        else:
            inventory.setdefault(addedItem[i], 1)
            
    print('Inventory: ' )
    count = 0
    for rep,m in inventory.items():
        print(m, ' ', rep)
        count += m
    print('Total number of items: ', count)
        
        


inv = {'gold coin': 42 , 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)



