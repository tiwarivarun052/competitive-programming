# [1 2 3] Print all SubArray of given array.
# def printSubArray(A, start, end):
#     for i in range(start, end+1):
#         print(A[i], end=" ")
#     print()
# def printAllSubArray(A):
#     n=len(A)
#     for i in range(n):
#         for j in range(i,n):
#             printSubArray(A, i, j)
# A=[1,2,3]
# printAllSubArray(A)


#  Print sum of every single Sub element.
# def printAllSubArray(A):
#     n=len(A)
#     for i in range(n):
#         for j in range(i,n):
#             sum_sub =0
#             for k in range(i, j+1):
#                 sum_sub += A[k]
#             print(sum_sub)
# A=[1,2,3]
# printAllSubArray(A)


#  Given an integer array "nums" . Find the sub array with largest sum and return its sum.
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# def maxSubArray(nums):
#     max_sum = nums[0]
#     n=len(nums)
#     for i in range(n):
#         current_sum = 0
#         for j in range(i,n):
#             current_sum += nums[j]
#             max_sum = max(max_sum, current_sum)
#     return max_sum
# print(maxSubArray(nums))
# Output: 6


# Q-1 :- Given an array. Find the sum of all sub arrays sum.

# Q-2 :- Given an integer array nums. Find the sub array with largest sum.
