# WAP to check if the last digit is 4.

num = int(input("Enter a number: "))

if num % 10 == 4:
	print(f"The last digit of {num} is 4.")
else:
	print(f"The last digit of {num} is not 4.")