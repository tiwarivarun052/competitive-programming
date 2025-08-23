# WAP to accept a number from 1 to 7 and display the name of the day, like 1 for 
# Sunday, 2 for Monday, etc. 

num = int(input("Enter a number (1-7): "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if 1 <= num <= 7:
	print(f"Day {num} is {days[num-1]}.")
else:
	print("Invalid input. Please enter a number from 1 to 7.")
