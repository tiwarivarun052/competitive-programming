# n = int(input("Enter:"))
# m = int(input("Enter:"))
# for i in range(0, n):
#     for j in range(0, m):
#         print("*", end="")
#     print()


# N = int(input("Enter: "))
# for i in range(N):
#     for j in range(N):
#         print("*", end="")
#     print()


# n = int(input("Enter: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end="")
#     print()


# n = int(input("Enter: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

# n = int(input("Enter: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(j%2==0):
#             print("*", end="")
#         else:
#             print(j, end="")
#     print()

# n = int(input("Enter: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(j==1 or j==n):
#             print("*", end="")
#         else:
#             print("_", end="")
#     print()

# n = int(input("Enter: "))
# for i in range(1, n+1):
#     print("*", end="")
#     for j in range(n+1-i):
#         print("_", end="")
#     print("*", end="")
#     print()

# n = int(input("Enter: "))
# for i in range(1, n+1):
#     for j in range(n,0,-1):
#         if(j>i):
#             print("_", end="")
#         else:
#             print("*", end="")
#     print()

# n = int(input("Enter: "))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print("_", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

n = int(input("Enter: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if(j<=n-i):
            print("*", end="")
        else:
            print("_", end="")
    print()