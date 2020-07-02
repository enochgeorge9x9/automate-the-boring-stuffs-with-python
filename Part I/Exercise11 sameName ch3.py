#sameName1
##def spam():
##    eggs = 'spam local'
##    print(eggs)
##
##def bacon():
##    eggs = 'bacon local'
##    print(eggs)
##    spam()
##    print(eggs)
##
##eggs = 'global'
##bacon()
##print(eggs)

#sameName2
#if you want a variable to be global-use the global statement
##def spam():
##    global eggs
##    eggs = 'spam'
##
##eggs='global'
##print(eggs)
##spam()
##print(eggs)

#sameName3
def spam():
    global eggs
    eggs = 'spam' #this is global

def bacon():
    eggs = 'bacon' #this is local
def ham():
    print(eggs) #this is local

eggs =42 #this is global
print(eggs)
spam()
print(eggs)
