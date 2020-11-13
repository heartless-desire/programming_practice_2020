import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 50
FPS = 24
LIVE = 1
DEAD = 0
VALUES = [LIVE, DEAD]


def random_grid(N):
    return np.random.choice(VALUES, N * N, p=[0.25, 0.75]).reshape(N, N)


def step(self, frame, grid, N):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 1)
            if grid[i, j] == LIVE:
                if total < 2 or total > 3:
                    new_grid[i, j] = DEAD
            else:
                if total == 3:
                    new_grid[i, j] = LIVE

    frame.set_data(new_grid)
    grid[:] = new_grid[:]
    return frame


grid = random_grid(N)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='none', cmap='spring_r')
anim = animation.FuncAnimation(fig, step, fargs=(img, grid, N),
                               frames=15,
                               interval=FPS,
                               save_count=150)

plt.show()
