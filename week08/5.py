import numpy as np


def non_nan_mat(mat):
    if np.all(np.isnan(mat)):
        mat[...] = 0
        return mat
    else:
        return np.nan_to_num(mat, nan=np.nanmean(mat))


n = np.random.randint(3, 10)
m = np.random.randint(3, 10)

values = np.random.random(size=10) * 10
values = np.append(values, np.nan)

a = np.random.choice(values, n * m, p=[0.08, 0.08, 0.08,
                                       0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.2]).reshape(n, m)

print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(non_nan_mat(a))
