# You are given an integer A, you need to find and return the sum of all the even numbers 
# between 1 and A. Even numbers are those numbers that are divisible by 2. 
# Input:- A = 5 
# Output:- 6 
# Explanation:- Even numbers between [1, 5] are (2, 4). 

A = int(input("Enter an integer A: "))
total = 0
i = 2
while i <= A:
	total += i
	i += 2
print(f"Sum of even numbers between 1 and {A} is {total}")

