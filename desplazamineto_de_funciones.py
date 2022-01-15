import numpy as np
import matplotlib.pyplot as plt

def f (x):
    return x**2

N= 1000 #numero de puntos
c= 5 #c : constante positiva de desplazamiento
x = np.linspace(-10,10, 1000) 
y=f(x) #funcion normal
up = f(x) + c #desplazamiento arriba
down = f(x) - c # desplasamiento abajo
right = f(x-c) # desplasamiento a la derecha
left = f(x + c) # desplasamiento a la isquierda.



fig, ax = plt.subplots(1,1,figsize=(10,10),dpi= 60)

ax.plot(x,y , label = "f(x)")
ax.plot(x, up, label = "f(x)+c")
ax.plot(x , down, label = "f(x)- c")
ax.plot(x , right, label = "f(x - c)")
ax.plot(x, left, label ="f(x + c)")

ax.scatter([-c,0,0,c], [0, -c , c ,0], color='red', s=100 ) #puntos en las 4 cordenadas
ax. grid()


ax.legend(loc=3, fontsize='x-large')
ax.axhline(y=0, color = 'y')
ax.axvline(x=0 , color = 'y')
ax.set_xlim(-10, 10) #limita los datos en x
ax.set_ylim(-6, 14) #limita los datos en y

plt.show()