import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if -5 <= x <= 5:
        return x**2
    elif x < -5:
        return 2*abs(x)-1
    elif x > 5:
        return 2*x
    else:
        raise ValueError


x = np.arange(-10, 11, 1)
y = []

for i in x:
    y.append(f(i))
    print(i)

plt.plot(x, y)
plt.show()
