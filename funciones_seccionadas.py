from math import pi
import numpy as np
import matplotlib.pyplot as plt

def H(X):
  Y = np.zeros(len(X))
  for idx,x in enumerate(X):
    print(idx, x) #gerea un indice de nuestro valor en x
    if x>=0:
      Y[idx] = 1.0
  return Y

# Datos para graficación

N = 1000
X = np.linspace(-1,1, num=N)
y = H(X)
fig, ax = plt.subplots()
ax.plot(X, y)
ax.grid()

plt.show()