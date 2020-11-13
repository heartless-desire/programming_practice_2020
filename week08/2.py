import numpy as np

a = np.arange(2, 75, 1)
print(a[1::2])
a[1::2] = -1
print(a)
