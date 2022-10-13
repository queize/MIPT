import numpy as np
from matplotlib import pyplot as plt
n = np.arange(10)
phi0 = np.deg2rad(0)
phi1 = np.deg2rad(45)
phi2 = np.deg2rad(70)
# V_A, V_B = 10, 20
# R_A, R_B = 30, 40
omega_A = 1
omega_B = 1.12
tA1 = ((phi1 + 2*np.pi*n) - phi0) / omega_A
tA2 = ((phi2 + 2*np.pi*n) - phi0) / omega_A
tB1 = ((phi1 + 2*np.pi*n) - (phi0 + 2*np.pi*(omega_B/omega_A - 1)*n)) / omega_B
tB2 = ((phi2 + 2*np.pi*n) - (phi0 + 2*np.pi*(omega_B/omega_A - 1)*n)) / omega_B
plt.plot(n, tA1, 'r')
plt.plot(n, tA2, 'r--')
plt.plot(n, tB1, 'b')
plt.plot(n, tB2, 'b--')

plt.grid()
plt.show()
