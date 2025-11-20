# Given a number A. Return square root of the number if it is perfect square otherwise return-1.
#  Note: A number is a perfect square if its square root is an integer
import math
def sqrt(A):
    root = int(math.sqrt(A))
    if root * root == A:
        return root
    return -1
print(sqrt(16)) 