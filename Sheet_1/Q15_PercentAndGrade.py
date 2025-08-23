# Accept the percentage from the user and display the grade according to the following 
# criteria. 
# ● 
# Below 25 – D 
# ● 
# 25 to 45 – C 
# ● 
# 45 to 65 – B 
# ● 
# 65 to 85 – A 
# ● 
# Above 85 – A+

percent = float(input("Enter your percentage: "))
if percent < 25:
	grade = "D"
elif percent < 45:
	grade = "C"
elif percent < 65:
	grade = "B"
elif percent < 85:
	grade = "A"
else:
	grade = "A+"
print(f"Your grade is {grade}.")
