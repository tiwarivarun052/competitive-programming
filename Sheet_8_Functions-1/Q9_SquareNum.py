# WAP to print square of all numbers from x to y
def sqnum(a, b):
    for i in range(a, b + 1):
        print(i * i)
x = int(input())
y = int(input())
sqnum(x, y)
