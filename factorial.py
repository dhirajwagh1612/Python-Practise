#basic function to get factorial using if else condition.
def factorial(n):
    if n ==1:
        return 1
    else:
        n *=(n-1)
        return n
    
factorial(12)

#find the factorial using iterative approatch.
def factorial(n):
    if n ==0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact *=(n-1)
            n -=1
        return fact
        
factorial(23)

# find factorial using for loop.
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *=i
    return res

factorial(21)


#by using ternary operator
def factorial(n):
    return 1 if (n==1 or n==0) else n *factorial(n-1)

factorial(21)

#using math function 
import math
def factorial(n):
    fact = math.factorial(n)
    return fact

factorial(34)

#using numpy
import numpy as np
def numpy_factorial_np(n):
    fact = np.prod([i for i in range (1, n+1)])
    return fact


