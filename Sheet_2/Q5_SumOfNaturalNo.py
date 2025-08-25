# Write a program to find the sum of all Natural numbers from 1-N,where you have to take N as input from user 
# Input:- N = 10 
# Output:- 55 

N = int(input("Enter a positive integer: "))
total = 0
i = 1
while (i <= N):
	total += i
	i += 1
print("Sum of natural numbers is : ", total)

