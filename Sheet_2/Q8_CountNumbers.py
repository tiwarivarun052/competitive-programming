# Take an integer N as input and print the count of digits of that number. 
# Input:- N = 10101 
# Output:- 5 
# Explanation:- 10101 has 5 digits 

N = int(input("Enter an integer N: "))
count = 0
num = abs(N)
if num == 0:
	count = 1
else:
	while num > 0:
		num //= 10
		count += 1
print(f"Number of digits in {N} is {count}")

