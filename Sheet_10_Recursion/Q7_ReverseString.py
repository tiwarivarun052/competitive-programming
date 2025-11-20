def revString(s):
    if len(s) == 0:
        return s
    return s[-1] + revString(s[:-1])

s = input()
print(revString(s))