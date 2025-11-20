# WAPtoimplement the Pythagoras Theorem in Python using functions.
import math
def theorem(a, b):
    return math.sqrt(a**2 + b**2)
a = int(input("a: "))
b = int(input("b: "))
print(theorem(a, b))
