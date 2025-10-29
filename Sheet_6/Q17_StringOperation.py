A = input()
A = A + A
A = ''.join(ch for ch in A if not ch.isupper())
vowels = 'aeiou'
A = ''.join('#' if ch in vowels else ch for ch in A)
print(A)