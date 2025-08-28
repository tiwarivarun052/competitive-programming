n = int(input("Enter: "))

for i in range(n):
    for j in range(i):
        print("_", end="")
    for j in range(n-i):
        print("*", end="")
    print()