# Accept the percentage from the user and display the grade according to the following criteria.
# Below 25 – D 
# 25 to 45 – C 
# 45 to 65 – B 
# 65 to 85 – A 
# Above 85 – A+

percent = float(input("Enter your percentage: "))
if percent < 25:
	print("Your grade is D.")
elif percent < 45:
	print("Your grade is C.")
elif percent < 65:
	print("Your grade is B.")
elif percent < 85:
	print("Your grade is A.")
else:
	print("Your grade is A+.")

