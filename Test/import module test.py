"""
import module test
"""
def fromModuleImport():
    """
    for math import sqrt only as function
    """
    from math import sqrt
    #import sqrt from math module only
    numberIn = float(input())
    sqrtCompute = sqrt(numberIn)
    print(int(sqrtCompute))
fromModuleImport()

def importLibraryAs():
    """
    shorten module name
    """
    import math as mt
    number = float(input())
    #shorten math module as "mt"
    print(int(mt.sqrt(number)))
importLibraryAs()
