import numpy as np
import time

SKIP_ONE_LINE = "\n\n"

size = 10000
loops = 1000
numNp = np.random.rand(size)
numList = numNp.tolist()

start = time.perf_counter()
for _ in range(loops):
    totalNp = np.sum(numNp)
end = time.perf_counter()
print(f"Elapse time of numpy.sum() = {end - start:.4f}")

start = time.perf_counter()
for _ in range(loops):
    totalList = sum(numList)
end = time.perf_counter()
print(f"Elapse time of sum() = {end - start:.4f}", end=SKIP_ONE_LINE)

data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"{data}", end=SKIP_ONE_LINE)

# data and dataT share the same data array, but with different iteration logic.
dataT = data.T
dataT[1][2] = 111
print(f"{dataT}")
print(f"dataT: {hex(id(dataT))}, type = {type(dataT)}")
print(f"data: {hex(id(data))}, type = {type(data)}")
print(f"{data}", end=SKIP_ONE_LINE)

ex1 = np.ones((5, 3))
ex2 = np.asarray(dataT)
print(ex1)
print(f"ex1: {hex(id(ex1))}, type = {type(ex1)}")
print(f"ex2: {hex(id(ex2))}, type = {type(ex2)}")
print(ex2, end=SKIP_ONE_LINE)

ex3 = np.empty((3, 5), dtype=int)
ex4 = ex3.astype(np.int16)
print(f"ex3: {hex(id(ex3))}, type = {type(ex3)}")
print(f"ex4: {hex(id(ex4))}, type = {type(ex4)}")
print(ex3)
print(ex4, end=SKIP_ONE_LINE)
