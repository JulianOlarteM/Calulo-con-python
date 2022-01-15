from math import pi
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.sin(x)

N=100
x = np.linspace(-2*pi, 2*pi, N)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()