n = int(input())
arr = list(map(int, input().split()))

L,R = map(int, input().split())
total = sum(arr[L-1:R])

print(total)