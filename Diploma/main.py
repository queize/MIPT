import numpy as np
from matplotlib import pyplot as plt

x = np.arange(10)

fig, ax = plt.subplots()
ax.plot(x, x**2, color='red', linestyle='--')

ax.grid(ls=':')
plt.show()


