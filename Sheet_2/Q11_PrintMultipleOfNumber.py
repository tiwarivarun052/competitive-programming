# Take a number A as input, print its multiplication table having the first 10 multiples. 
# Input:-3 
# Output:- 
# 3 * 1 = 3 
# 3 * 2 = 6 
# 3 * 3 = 9 
# 3 * 4 = 12 
# 3 * 5 = 15 
# 3 * 6 = 18 
# 3 * 7 = 21 
# 3 * 8 = 24 
# 3 * 9 = 27 
# 3 * 10 = 30

A = int(input("Enter a number A: "))
i = 1
while i <= 10:
	print(f"{A} * {i} = {A * i}")
	i += 1

