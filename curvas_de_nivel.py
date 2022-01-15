''' 
Para estudiar matplotlib:
https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html


'''
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return np.sin(x) + 2*np.cos(y)

res = 1000
x = np.linspace(-4,4,num=res)
y = np.linspace(-4,4,num=res)

x, y = np.meshgrid(x,y) # realiza a combinacion de puntos de x, y
z =  f(x,y) # obtenemos nuestra funcion.

'''
GRAFICANDO NUESTRA FUNCION MULTIVARIBLE:
'''
fig, ax = plt.subplots(subplot_kw={"projection":"3d"}) # creamos nuestros ejes. tipo de subplot.
surf = ax.plot_surface(x,y,z, cmap=cm.cool) #le generamos nuestras variables, y nuestro mapa de color.
fig.colorbar(surf) #barraa de color.

'''
GRAFICANDO NUESTRAS CURVAS DE NIVEL:
'''
fig2, ax2 = plt.subplots()
level_map = np.linspace(np.min(z),np.max(z),num=res) #creamos un vector desde mi valor minimo de z hasta el valor maximo de z

cp = ax2.contourf(x,y,z, levels = level_map, cmap=cm.cool)
fig2.colorbar(cp)

plt.show() 