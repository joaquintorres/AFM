from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
#import random as rm
#import math

# ARMADO DE LA GRILLA:
h = 100 # Altura en nm
dim = 1000 # Cantidad de píxeles para un "pitch"
A = np.zeros((dim,dim)) # Este es el "pitch" patrón, después lo voy a concatenar ya que la grilla es periódica

for i in range(0, dim):
    if 0.15*dim <= i < (0.15+0.70)*dim:
        for j in range(0, dim):
            if 0.15*dim <= j < (0.15+0.70)*dim:
                A[i,j] = h
    else:
        A[i,:] = 0

p = 1 # p^2 va a ser el número de pitch's total luego de concatenar

R = np.concatenate((A,) * p) # Primera concatenación: un "pitch" debajo del otro
G = np.concatenate((R,) * p, axis=1) # Al "rectangulo" R lo concateno uno al lado del otro: obtengo la grilla G
 
#########################################
px = dim*p # Los píxeles (elementos de matriz) de una línea de grilla

t_linea = 1 # 1 segundo por línea
t_punto = t_linea/px

k  = 1 # Constante del resorte (cantilever "lineal")
Kp = 1.95 # Constante Proporcional del controlador PID
SP = 50 # Setpoint en nanonewton

G0 = G[0,0] # Primer punto de la grilla donde el cantilever alcanzó el setpoint y está en equilibrio.
            # Empieza a barrer de arriba hacia abajo, de izquierda a derecha

f = np.zeros((px, px)) # Matriz de mediciones de fuerza
e = np.zeros((px, px)) # Matriz de desviaciones respecto al setpoint
u = np.zeros((px, px)) # Matriz de correcciones dada una desviación
z = np.zeros((px, px)) # Matriz de alturas (topografía)

U = np.zeros(px) # Para cada línea, voy sumando a medida que barro las correcciones del lazo
Z = np.zeros(px) # Es parecida a U en su construcción sólo que cambia el signo: si hay una depresión en la topografía (altura "NEGATIVA"), el lazo habrá corregido con una fuerza POSITIVA (hacia arriba tal que deflecte el cantilever).

f[0, 0] = SP + k * (G[0,0] - G0) + U[0] # Acá el sensor mide la fuerza instantánea y la guarda
e[0, 0] = SP - f[0, 0] # A partir de la fuerza medida, calcula la desviación respecto al setpoint
u[0, 0] = Kp * e[0, 0] # De esa desviación, aplica una corrección proporcional

for i in range (0, px): # Fila i (de arriba hacia abajo)
    for j in range(0, px): # Para la fila i, barro en j (de izquierda a derecha)
        f[i, j] = SP + k * (G[i,j] - G0) + U[i] # Mido la fuerza en la posición (i,j). Al setpoint le sumo cuánto comprime
                                                # la muestra al resorte-cantilever y las correcciones del lazo
        e[i, j] = SP - f[i, j] # La desviación respecto al setpoint en la posición (i,j)
        u[i, j] = Kp * e[i, j] # Para esa desviación, el lazo corrije restando una fuerza (si mide una fuerza mayor al SP)
        U[i] = U[i] + u[i, j] # Voy sumando las correcciones del lazo para sumarlas a la mediciones de fuerza f: no solo la topografía
                              # contribuye a la fuerza medida
        Z[i] = Z[i] - u[i, j] # Para cada linea sumo las correciones (con signo corregido) hechas hasta los primeros j pixeles barridos.
        z[i, j] = Z[i]/k # Hasta ahora todas las mediciones eran de fuerza, como lo modelo con un resorte paso la fuerza a distancia

### Ploteo la grilla y la topografía barrida
fig, (ax1, ax2) = plt.subplots(1, 2)

images = [0, 0]
images[0] = ax1.imshow(G, cmap=plt.cm.gray) # Grilla
images[1] = ax2.imshow(z, cmap=plt.cm.gray) # Topografía

# Calculos los valores mínimo y máximo para todas las matrices, así delimito bien el rango del colorbar
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

# Escala de grises para la altura z
cbar = fig.colorbar(images[0], ax=(ax1, ax2))
cbar.set_label(r'altura (mm)', y=0.5, fontsize=10)

#plt.plot(z[300,:])
#print(f[300,140:155])

plt.show()
