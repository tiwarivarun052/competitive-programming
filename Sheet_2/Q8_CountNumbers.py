# Take an integer N as input and print the count of digits of that number. 
# Input:- N = 10101 
# Output:- 5 
# Explanation:- 10101 has 5 digits 

N = int(input("Enter a number: "))

count = 0


while (N > 0):
    N = N // 10   # remove last digit
    count += 1

print("Number of digits is : ", count)


