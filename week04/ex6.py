import numpy as np
from functools import reduce as rd
from numpy import pi
import matplotlib.pyplot as plt

# Setting Up
plt.rcParams.update({'font.size': 8})

# Value Preparing
a = 0.5
b = 3
n = np.arange(0, 20, 1)

x = np.arange(-2, 2, 0.001)
y = 0

for i in n:
    y += pow(a, i) * np.cos(pow(b, i) * pi * x)

# Plotting
plt.plot(x, y)
plt.axis('equal')
plt.xlabel(r'$x$')
plt.ylabel(r'$W(x)$')
plt.title(r'$W(x)=\sum_{n=1}^{10} a^{n}*\cos(b^{n}*\pi*x)$')
plt.show()