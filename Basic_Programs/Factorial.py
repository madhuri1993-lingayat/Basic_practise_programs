

# won logic

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        #print('factorial is')
        return n * fact(n-1)

f = fact(2)
print(f)
# factorial logic is:
# 4! = 4*3*2*1
#Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.


import sys
sys.exit()

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)

fact = factorial(6)
print(fact)
