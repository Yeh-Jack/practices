# Print diamond.
space = "  "
star = "* "
rows = 6

# Version 1 : 2 loops for 2 half triangles with double spaces.
for row in range(0, rows + 1):
    print(space * (rows - row) + star * (row * 2 - 1))
for row in range(rows - 1, 0, -1):
    print(space * (rows - row) + star * (row * 2 - 1))
print()

# Version 2 : single loop with single space.
space = " "
for row in range(-rows, rows + 1):
    sp = abs(row)
    print(space * sp, end="")
    st = rows - abs(row)
    print(star * st, end="")
    print()

# Version 3 : single loop with double spaces.
space = "  "
for row in range(-rows, rows + 1):
    sp = abs(row)
    print(space * sp, end="")
    st = rows - abs(row)
    print(star * (st * 2 - 1), end="")
    print()
print()

# # Multipulation table.
# for x in range(1, 10, 3):
#     y = x + 1
#     z = y + 1
#     for j in range(1, 10):
#         print("%s * %s = %2s" % (x, j, x * j), end="\t")
#         print("%s * %s = %2s" % (y, j, y * j), end="\t")
#         print("%s * %s = %2s" % (z, j, z * j), end="\n")
#     print()
