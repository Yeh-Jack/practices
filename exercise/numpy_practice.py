import numpy as np

# Method 1 : Append each row and reshape it.
ds = np.array(range(6))
for i in range(10, 60, 10):
    ds = np.append(ds, range(i, i + 6))
ds = np.reshape(ds, [6, 6])

# Method 2 :
# 1. Generate 60 sequencial numbers in one dimension array.
# 2. Reshape it to 6 * 10 2-dimension array.
# 3. Extract all rows with 0 ~ 6 columns.
ds = np.arange(60).reshape([6, 10])[:, :6]
print(ds)

print("=====  四個角落  =====")
# corner = ds[np.ix_([0, 5], [0, 5])]
corner = ds[::5, ::5]
print(corner)
print()
print("=====  中間交集  =====")
itsc = ds[2:4, 3:5]
print(itsc)
print("=====================")
