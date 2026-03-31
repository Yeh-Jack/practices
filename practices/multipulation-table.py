# Print diamond.
space = " "
star = "*"
width = 6
for row in range(0, width):
    for sp in range(0, width - row):
        print(space, end="")
    for st in range(0, row):
        print(star, end="")
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
