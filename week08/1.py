import time
import numpy as np
import random
import matplotlib.pyplot as plt
N = random.randint(3, 10)


def test_numpy_array():
    start_time = time.perf_counter()
    x = np.array(np.random.randint(10, 100, size=150))
    y = np.array(np.random.randint(10, 100, size=150))
    z = 2 * x**2 + 4 * y
    ans = (time.perf_counter() - start_time)
    return ans


def test_python_array():
    start_time = time.perf_counter()
    x = [random.randint(10, 100) for _ in range(151)]
    y = [random.randint(10, 100) for _ in range(151)]
    z = [2 * i**2 + 4 * j for i, j in zip(x, y)]
    ans = (time.perf_counter() - start_time)
    return ans


def test_numpy_matrix():
    start_time = time.perf_counter()
    A = np.floor(10 * np.random.random((N, N)))
    B = np.floor(10 * np.random.random((N, N)))
    C = A * B
    return time.perf_counter() - start_time


def test_python_matrix():
    start_time = time.perf_counter()
    A = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]
    C = [[i * j for i, j in zip(k, l)] for k, l in zip(A, B)]
    return time.perf_counter() - start_time


numpy_data = [test_numpy_array(), test_numpy_matrix()]
python_data = [test_python_array(), test_python_matrix()]
plt.plot(numpy_data, label='numpy')
plt.plot(python_data, label='python')
plt.legend(loc='best')
plt.grid(1)
plt.show()
