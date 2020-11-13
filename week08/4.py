import numpy as np

N = np.random.randint(10, 101)

a = np.floor(10 * np.random.random((N, N)))
b = a.copy()
print(a, a.sum(), a.max(), sep='\n')
print(a / a.max())
for i in range(len(b)):
    b[i] -= b[i].mean()
print(b)
a[np.unravel_index(a.argmax(), a.shape)] = -1
print(a)
