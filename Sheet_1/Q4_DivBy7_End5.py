# WAP to check if the number is divisible by 7 or if the last digit is 5. 

num = int(input("Enter a number: "))

if num % 7 == 0 or num % 10 == 5:
	print("divisible by 7 or last digit is 5.")
else:
	print("not divisible by 7 and last digit is not 5.")
