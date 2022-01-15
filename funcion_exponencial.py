from math import pi
import numpy as np
import matplotlib.pyplot as plt


def f(x):
  return np.e**x

x = np.linspace(-1, 1, num=100000)

y = f(x)

delta = 0.01

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.set_ylim(1 - delta,1 + delta)
ax.set_xlim(0 - delta, 0 + delta)
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()