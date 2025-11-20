def digitSum(n):
    if n == 0:
        return 0
    return n % 10 + digitSum(n // 10)

n = int(input())
print(digitSum(n))