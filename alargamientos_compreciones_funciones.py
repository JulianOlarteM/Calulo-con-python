import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.sin(x)
N = 1000
c = 3

x = np.linspace(-15,15, num=N)

y = f(x) * c
alarg_v = f(x) * c
comp_v = f(x) * 1/c #comprime verticalmente
comp_h = f(x*c)
alarga_h = f(1/c * x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.plot(x, alarg_v)
ax.plot(x, comp_v)
ax.plot(x, comp_h)
ax.plot(x, alarga_h)
ax.grid()

ax.legend(loc=3, fontsize='x-large')
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()