import numpy as np
import matplotlib.pyplot as plt

# Value preparing
x = np.arange(-10, 10, 1)
y = x * x - x - 6

# Plotting
plt.plot(x, y)
plt.show()
