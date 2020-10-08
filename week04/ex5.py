import numpy as np
import matplotlib.pyplot as plt

# Value preparing
x = np.array((1, 2, 3, 4, 5, 6))
y = np.array((.93, 1.3, 1.96, 2.1, 2.04, 2.7))

# Making Polynomial 1
p, v = np.polyfit(x, y, deg=1, cov=True)
polynomial_1 = np.poly1d(p)
y_p1 = polynomial_1(x)
# Making Polynomial 2
p2, v = np.polyfit(x, y, deg=2, cov=True)
polynomial_2 = np.poly1d(p2)
y_p2 = polynomial_2(x)

# Plotting
plt.plot(x, y, '--o', label=r'$y$')
plt.plot(x, y_p1, 'r-', label=r'$ax+b$')
plt.plot(x, y_p2, label=r'$ax^2+bx+c$')
plt.legend(loc='best')
plt.xlim([x[0]-1, x[-1]+1])
plt.show()
