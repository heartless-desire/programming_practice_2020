import numpy as np

n = np.random.randint(3, 10)
m = np.random.randint(3, 10)

a = np.random.randint(-10, 10, size=(n, m))

b = int(input('column number:')) - 1

print(a)

c = a[np.argsort(a[:, b])]

print(c[::-1][:m])
