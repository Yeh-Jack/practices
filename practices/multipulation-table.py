# Multipulation table.
for i in range(1, 10, 3):
    x = i
    y = x + 1
    z = y + 1
    for j in range(1, 10):
        print("%s * %s = %2s" % (x, j, x * j), end="\t")
        print("%s * %s = %2s" % (y, j, y * j), end="\t")
        print("%s * %s = %2s" % (z, j, z * j), end="\n")
    print()
