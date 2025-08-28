n = int(input("Enter: "))

for i in range(1, n+1):
    for j in range(n,0,-1):
        if(j>i):
            print("_", end="")
        else:
            print("*", end="")
    print()
