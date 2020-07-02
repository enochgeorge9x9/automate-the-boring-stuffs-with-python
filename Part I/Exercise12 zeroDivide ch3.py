#error handling
##def spam(divideBy):
##    return (42/divideBy)
##
##print(spam(2))
##print(spam(33))
##print(spam(0))
##print(spam(1))
##

#try and except
def spam(divideBy):
    try:
        return (42/divideBy)
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(33))
print(spam(0))
print(spam(1))

