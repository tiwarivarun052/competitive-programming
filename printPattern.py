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


n = int(input("Enter: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print()