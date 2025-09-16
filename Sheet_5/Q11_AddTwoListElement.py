A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
sum = []
for i in range(len(A1)):
    sum.append(A1[i] + A2[i])
print(sum)