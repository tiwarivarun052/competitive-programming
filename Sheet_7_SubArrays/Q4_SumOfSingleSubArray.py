n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += arr[j]
    print(current_sum)