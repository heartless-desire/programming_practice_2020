import numpy as np

a = np.random.randint(0, 100, size=10)

print(a)

b = int(input())

print(abs((a - b)).min() + b)
