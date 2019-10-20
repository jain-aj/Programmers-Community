# Python program to check a number is EVEN or ODD

def isEven(n) :
    return (int(n / 2) * 2 == n)

n = int(input("Enter a number : "))
if(isEven(n) != False):
    print ("EVEN")
else :
    print ("ODD")
