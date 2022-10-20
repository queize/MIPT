import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x, y = np.meshgrid(np.linspace(1, 5, 100), np.linspace(1, 5, 100))
z = np.log(np.cos(np.exp(x + y))) - np.log(x*y)
ax.plot_surface(x, y, z)
ax.grid()