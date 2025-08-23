# Write a program to input three numbers(A, B & C) from the user and print the 
# minimum element among A, B & C. 

A = float(input("Enter first number (A): "))
B = float(input("Enter second number (B): "))
C = float(input("Enter third number (C): "))
minimum = min(A, B, C)
print(f"The minimum of {A}, {B}, and {C} is {minimum}.")
