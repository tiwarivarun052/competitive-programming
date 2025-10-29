A = input()
words = A.split()
reverse_words = [word[::-1] for word in words]
result = " ".join(reverse_words)
print(result)