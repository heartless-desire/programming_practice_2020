import numpy as np

n, m = list(map(int, input('Matrix size:').split()))

a = int(input('Inner filling:'))
b = int(input('Outer filling:'))

z = np.zeros((n, m))

z += a

z[:, 0] = z[0, :] = z[n - 1, :] = z[:, m - 1] = b
print(z)
