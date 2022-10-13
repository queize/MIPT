import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

h = 0.1
T = 1000
mu = 398600.4415 * 1e9
t = np.arange(0, T + h, h)

def f(x):
    r = x[:3]
    v = x[3:]
    return np.concatenate([
        v,
        -mu*r/np.linalg.norm(r)**3
    ])


def adams(x):
    pass


def rk4(x):
    k1 = f(x)
    k2 = f(x + h*k1/2)
    k3 = f(x + h*k2/2)
    k4 = f(x + h*k3)
    return x + (k1 + 2*k2 + 2*k3 + k4)*h/6


N = t.shape[0]
X = np.zeros((6, N))
X0 = np.array([42158.6, -687.006, 0, 0.0500973, 3.07425, 0]) * 1e3
X[:, 0] = X0

for i in range(1, N):
    X[:, i] = rk4(X[:, i - 1])

x = X[0, :]
y = X[1, :]
z = X[2, :]

data = pd.DataFrame(X)
data.to_csv('new_data.csv')