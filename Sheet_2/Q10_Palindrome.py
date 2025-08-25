#  You are given an integer A as input, and you need to determine whether it is a palindrome 
# or not. A palindrome integer is one whose digits, when reversed, result in the same number. 
# For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome 
# because its reverse is 321.Note: The given integer will not have any leading zeros. 
# Input:- A = 131 
# Output:- Yes 
# Explanation:- For A = 131, reverse(A) = reverse(131) = 131, which is the same as A. 


A = input("Enter a word or number: ")

if A == A[::-1]:
    print("palindrome.")
else:
    print("not a palindrome.")
