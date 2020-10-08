import numpy as np
import matplotlib.pyplot as plt

# Setting Up
plt.rcParams.update({'font.size': 6})

# Value preparing
x = np.arange(-10, 10, 1)

y = np.log((x**2 + 1) * np.exp(-abs(x) / 10)) / \
    np.log(1 + np.tan(1 / (1 + (np.sin(x))**2)))

# Plotting
plt.plot(x, y)
plt.show()
