# Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
# input from user 
# Input:- N = 10 
# Output:- 55 

N = int(input("Enter a positive integer N: "))
total = 0
i = 1
while i <= N:
	total += i
	i += 1
print(f"Sum of natural numbers from 1 to {N} is {total}")

