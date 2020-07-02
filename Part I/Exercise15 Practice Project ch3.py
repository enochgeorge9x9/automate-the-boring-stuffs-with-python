#Collatz Sequence
def collatz(number):
    if number %2 ==0:
        n= number // 2
        print(n)
        return(n)
    elif number%2 == 1:
        m = 3*number+1
        print(m)
        return m
try:
    p = input("Enter a number: ")
    while int(p) != 1:
        p = collatz(int(p))
except ValueError:
    print("Try an integer!")
    
    

    
