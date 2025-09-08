n = int(input("Enter : "))

for i in range(1, n+1):
    if i == (n // 2) + 1:
        print("*")
    else:
        print("* *")
