# Given an array of 'A' non negative numbers and the non negative number 'B'.
#We need to find sum of subarray 'A' with its sum less than 'B'.

# A = [2, 5, 6]
# B = 10
# count = 0
# arr=len(A)
# for i in range(arr):
#     sum = 0
#     for j in range(i, arr):
#         sum+=A[j]
#         if sum < B:
#             count += 1
# print(count)
# Output: 8


# Given an array of integer 'A.' subarray of array is said to be good if it fulfills anyone of the criteria : 
# 1:-  length of subarray is to be even.
# And sum of all elements of subarray must be less than B.

# 2:- length of subarray is to be odd.
# And sum of all elements of subarray must be greater than B.

# your task is to count number of good subarrays in 'A'.

# A = [2, 5, 6]
# B = 10
# count = 0
# arr= len(A)
# for i in range(arr):
#     sum = 0
#     for j in range(i, arr):
#         sum+=A[j]
#         l = j - i + 1
#         if (l % 2 == 0 and sum < B) or (l % 2 != 0 and sum > B):
#             count += 1
# print(count)

# You have given an integer array 'C' of size 'A'.
# Now you need to find its subarray so that the sum of continuous element is maximum.
# But the sum must not exceed 'B'.

# Example 1 :-
C = [2, 5, 6]
B = 10
max = 0
for i in range(len(C)):
    sum = 0
    for j in range(i, len(C)):
        sum+=C[j]
        if sum <= B and sum > max:
            max = sum
print(max)

# Example 2 :-
C = [2, 1, 3, 4, 5]
B = 12
max = 0
for i in range(len(C)):
    sum = 0
    for j in range(i, len(C)):
        sum+=C[j]
        if sum <= B and sum > max:
            max = sum
print(max)

# Example 3 :-
C = [2, 2, 2]
B = 1
max = 0
for i in range(len(C)):
    sum = 0
    for j in range(i, len(C)):
        sum+=C[j]
        if sum <= B and sum > max:
            max = sum
print(max)

# Given an array A of length N, your task is to find maximum possible sum of any non empty contiguous subarray.
# In other words, among all possible of subarrays of A determined the one the highest sum and return its sum.
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = A[0]
current_sum = 0
for num in A:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print(max_sum)