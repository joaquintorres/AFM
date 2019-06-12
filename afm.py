'''
Archivo que arma las grillas.
'''

import numpy as np
import matplotlib.pyplot as plt
#import random as rm
#import math

plt.close('all')

# ARMADO DE LAS GRILLAS:
h = 100 # Altura en nm
dim = 100 # Cantidad de píxeles para un "pitch"
A = np.zeros((dim,dim)) # Este es el "pitch" patrón, después lo voy a concatenar ya que la grilla es periódica

for i in range(0, dim):
    if 15 <= i < 15+70:
        for j in range(0, dim):
            if 15 <= j < 15+70:
                A[i,j] = h
    else:
        A[i,:] = 0

p = 5 # Cuántos "pitch's" voy concatenar al armar la grilla

R = np.concatenate((A,) * p) # Primera concatenación: un "pitch" debajo del otro
G = np.concatenate((R,) * p, axis=1) # Al "rectangulo" R lo concateno uno al lado del otro: obtengo la grilla G

# Ploteo la grilla
plt.figure()

plt.imshow(G, cmap=plt.cm.gray) # Escala de grises

cbar = plt.colorbar()
plt.clim(-10, 120)
cbar.set_label(r'altura (mm)', y=0.5, fontsize=10)

plt.show()

#%%

setpoint = 110 

e_t = []
T_loop = []

pixeles = 450
total = 700 # Tiempo total en recorrer cada linea. #¿UNIDADES? 
tiempo_por_pixel = total/pixeles
respuesta_lazo = 0.1 # Representa el tiempo que le toma al lazo corregir. Tiene que ser menor que el tiempo por pixel.

## ------------------ ** ------------------ ##

'''
De esta manera el lazo logra corregirse 2 veces en cada posición.
Cantidad de correcciones esta dada por:
    a) tiempo que estoy en cada pixel,
    b) tiempo de respuesta del lazo.
En este caso como el tiempo que esta en cada pixel es mayor al tiempo de respuesta del
lazo, logra corregir la altura mas de  una vez antes de cambiar de posición.
'''

N = int(tiempo_por_pixel/respuesta_lazo)

#%%
# Condiciones iniciales.
distancia_canti_muestra = setpoint
foto_scaneada = np.eye(40)
K_p = 1.96
K_i = 0.76
t_loop = 0

print('\n')

for i in range (len(A)):
    for j in range (len(A)):
        distancia_canti_muestra = distancia_canti_muestra - A[i][j]
        for _ in range (N):
            e_t.append (setpoint - distancia_canti_muestra) 
            T_loop.append (t_loop)
            e_t_i = sp.integrate.simps (e_t,T_loop)
            e_t_p = setpoint - distancia_canti_muestra
            distancia_canti_muestra = distancia_canti_muestra + K_p * e_t_p + K_i * e_t_i
            t_loop = t_loop + respuesta_lazo
        #foto_scaneada[i][j] = distancia_canti_muestra # ¿Qué es esto?
    
    print('\rSimulando la línea: %3d de %3d'%(i,dim),end='')
#%%
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8, 8))
plot_grilla = ax1.imshow(grilla,cmap = "GnBu")
plot_fot_scaneada = ax2.imshow(foto_scaneada,cmap = "GnBu")

ax1.set_title ("Simulación de una \n muestra original")
ax2.set_title ("Simulación de una \n muestra scaneada")

ax1.set_xlabel ("Posición en x")
ax2.set_xlabel ("Posición en x")

ax1.set_ylabel ("Posición en y")
ax2.set_ylabel ("Posición en y")

## ------------------ ** ------------------ ##
posicion_barra = fig.add_axes([1.03,0.29,0.03,0.42])
fig.colorbar(plot_fot_scaneada, cax=posicion_barra)

fig.tight_layout()
textstr = '\n'.join((
    r'$Kp=%.2f$' % (K_p, ),
    r'$Ki=%.2f$' % (K_i, ),
    r'$Setpoint=%.2f%s$' % (setpoint,"nm")))

fig.text (0.08,0.15, textstr,fontsize=12)
fig.savefig('5.Simulacion muestra scaneada.png', bbox_inches="tight")
plt.show ()
