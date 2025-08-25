# Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
# given number N. 
# Input:- N = 1589 
# Output:- 23 
# Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.

N = int(input("Enter an integer N: "))
total = 0
while (N > 0):
	total = total + (N % 10)
	N //= 10
print("Sum of digits is : ", total)

