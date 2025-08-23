# Read three angles of triangles and determine their types(Right triangle, Obtuse 
# triangle, Acute triangle). 

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))
if a + b + c != 180 or a <= 0 or b <= 0 or c <= 0:
	print("Not a valid triangle.")
elif a == 90 or b == 90 or c == 90:
	print("Right triangle")
elif a > 90 or b > 90 or c > 90:
	print("Obtuse triangle")
else:
	print("Acute triangle")
