# utilidad en los decibelios
from math import pi
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.log10(x)

N = 1000
x = np.linspace(0.01, 1000, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()