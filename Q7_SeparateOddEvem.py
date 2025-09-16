A = list(map(int, input().split()))
even = []
odd = []
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:", even)
print("Odd:", odd)