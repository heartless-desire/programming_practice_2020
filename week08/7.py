import numpy as np


a = np.random.randint(0, 100, size=10)

print(a)

with open('file', 'wb') as f:
    np.save(f, a)

with open('file', 'rb') as f:
    b = np.load(f)

print(b)
