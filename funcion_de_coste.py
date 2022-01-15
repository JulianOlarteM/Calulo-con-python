from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

#FUNCION 
def  f(x,y):
    return x**2 + y**2

#GRAFICACION DE LA FUNCION EN 3D
res = 100
fig1, ax1 = plt.subplots(subplot_kw = {"projection": "3d"})
x=np.linspace(-4,4,res)
y=np.linspace(-4,4,res)
X,Y = np.meshgrid(x,y)  
Z=f(X,Y)
surf = ax1.plot_surface(X,Y,Z, cmap=cm.cool)
fig1.colorbar(surf)

#GENERANDO EL CONTORNO DE LA FUNCION EN 2D (X,Y)
fig2, ax2 = plt.subplots()
level_map = np.linspace(np.min(Z),np.max(Z),res)
cp = ax2.contourf(X,Y,Z,levels= level_map, cmap=cm.cool)
fig2.colorbar(cp)
plt.title("Desenso del gradiente")



#DERIVADAS PARCIALES
def derivada (_p,p):
    return (f(_p[0], _p[1]) - f(p[0], p[1]) / h) #definicion formail de la derivada "f((x+deltax) - f(x) / deltax"


#GENERAMOS UN PUNTO ALEATORIO EN NUESTRO IMAEN DE CONTORNO
p=np.random.rand(2) * 8 - 4 # punto aleatorio entre -4 y 4 (. rand arroja un valor entre 0 y 1, le asignamos 2 por la funcion es bodimencional de dos componentes. x y)
print(p)
plt.plot(p[0], p[1], 'o',c='k')
lr = 0.01
h = 0.01
grad = np.zeros(2)
for i in range(10000):
    for idx, val in enumerate(p): 
        print(idx,val)
        _p = np.copy(p)
        _p[idx] = _p[idx] + h
        dp = derivada(_p,p) 
        grad[idx] = dp
    p = p - lr * grad
    if(i % 10 == 0):
        plt.plot(p[0],p[1],'o', c='r')
plt.plot(p[0],p[1],'o', c='w')
plt.show()

print("El punto mínimo se encuentra en: ", p)

'''
#GRADIENTE
def gradiente (p):
    deltax=0.01
    grad =  np.zeros(2) #un vector lleno de zeros, con dos componentes.
    for idx, val in enumerate(p):
        cp = np.copy(p) #generamos una copia de p
        cp[idx] = cp[idx] + deltax #agragamos el deltax
        dp = derivada(cp , p, deltax)
        grad[idx] = dp
    return grad


#Debemos hacer que nuestro punto decienda a nuestro valore minimo de a pasaos pequeños (gradiente del punto)
lr= 0.01
for i in range (1000):
    p = p - lr*gradiente(p)
    if(i % 10 == 0):
        plt.plot(p[0], p[1], 'o',c='r')
plt.plot(p[0], p[1], 'o',c='w')
plt.show()
'''



