# Print the pattern shown in your image (user inputs rows and columns)

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# basic validation
if m < 3 or n < 3:
    print("Please enter rows and columns >= 3.")
    raise SystemExit

# largest number of stars at each side (near the top)
max_side = n // 2 - 1
if max_side < 1:
    max_side = 1

inner_rows = m - 2          # rows excluding top and bottom
half = inner_rows // 2      # midpoint index of the inner rows

# top full row
print("*" * n)

# inner rows: side blocks taper from max_side down to 1, then mirror
for i in range(1, inner_rows + 1):   # i = 1 .. inner_rows
    if i <= half:
        side = max_side - (i - 1)
        if side < 1:
            side = 1
    else:
        # mirror for the lower half
        j = inner_rows - i + 1
        side = max_side - (j - 1)
        if side < 1:
            side = 1

    mid_spaces = n - 2 * side
    if mid_spaces < 0:        # safety: ensure spacing non-negative
        side = n // 2
        mid_spaces = n - 2 * side

    print("*" * side + " " * mid_spaces + "*" * side)

# bottom full row
print("*" * n)

