# You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell 
# whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 
# 180. 

A = int(input("Enter first angle: "))
B = int(input("Enter second angle: "))
C = int(input("Enter third angle: "))
if A + B + C == 180:
	print("The triangle is valid.")
else:
	print("The triangle is not valid.")
