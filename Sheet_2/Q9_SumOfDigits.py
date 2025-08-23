# Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
# given number N. 
# Input:- N = 1589 
# Output:- 23 
# Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.

N = int(input("Enter an integer N: "))
total = 0
num = abs(N)
while num > 0:
	total += num % 10
	num //= 10
print(f"Sum of digits of {N} is {total}")

