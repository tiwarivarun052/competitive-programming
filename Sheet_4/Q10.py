n = int(input("Enter : "))
for i in range(n, 0, -1):
    for j in range(2*i-1):
        print("*", end=" ")
    print()