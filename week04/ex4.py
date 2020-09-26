import numpy as np
import matplotlib.pyplot as plt

# Value preparing
x = np.arange(-50, 50, 1)
y = eval(input())

# Plotting
with plt.xkcd():
    plt.plot(x, y)

plt.show()
