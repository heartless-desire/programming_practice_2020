import numpy as np

n = int(input('matrix shape:'))

a = np.zeros((n, n))

print(a)


for i in range(n):
    z = 1 if not i % 2 else 0
    a[i][z::2] = a[i][z::2] + 1
print(a)
