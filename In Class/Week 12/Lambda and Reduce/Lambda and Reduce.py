#import module
from functools import *

reduce(lambda x,y : x*y, range(1,10), 2)

#reduce == code reduction method

#lambda == define function as (in short function)

#x,y == variable

#x*y == Process 1

#range(1,10) == Process 2

#2 == Process 3 (Optional)

#-----------------------------------------------------------------
#        v v Argument
def process1(x,y):
    return x*y #Process 1
#for define as function old method.

def process2(z): #Process 2
    for i in range(1,10):
        #(x*y) * 1
        #(x*y) * 2
        #(x*y) * 3
        #...
        #(x*y) * 10
    return z

def process3(w): #Process 3 (Optional)
    #(z1*2)
    #(z2*2)
    #(z3*2)
    #...
    #(z10*2)
    return w

#print value
print(w)
#-----------------------------------------------------------------
