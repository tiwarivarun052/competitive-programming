n = int(input())
arr = list(map(int, input().split()))
total_sum = 0
for i in range(n):
    contribution = arr[i] * (i + 1) * (n - i)
    total_sum += contribution
print(total_sum)


