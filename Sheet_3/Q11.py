m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

if m < 3 or n < 3:
    print("Please enter rows and columns >= 3.")
    raise SystemExit

max_side = n // 2 - 1
if max_side < 1:
    max_side = 1

inner_rows = m - 2          
half = inner_rows // 2      

print("*" * n)
for i in range(1, inner_rows + 1):
    if i <= half:
        side = max_side - (i - 1)
        if side < 1:
            side = 1
    else:
        j = inner_rows - i + 1
        side = max_side - (j - 1)
        if side < 1:
            side = 1

    mid_spaces = n - 2 * side
    if mid_spaces < 0: 
        side = n // 2
        mid_spaces = n - 2 * side

    print("*" * side + " " * mid_spaces + "*" * side)
print("*" * n)

