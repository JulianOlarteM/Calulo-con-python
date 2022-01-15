import matplotlib.pyplot as plt   # librería para graficar
import numpy as np                # librería para manejo de vectores y utilidades matemáticas

def f(x):
    return x**2

N = 100 #numero de puntos.
x = np.linspace(-10.0, 10.0, num = N) #Genera 100 valores que varian de -10 a 10
y = f(x)

fig, ax = plt.subplots() #genera una grafica de dos ejes vacia
ax.plot(x, y) #agrega la funcion especifica
ax.grid() # agrega una cuadrocula''
ax.axhline(y=0, color='r') # agraga una linea horizontal en y=0
ax.axvline(x=0, color='r') # agrega una linea vertica en x= 0

plt.show()