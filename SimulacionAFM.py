'''
Simulación del otro grupo:

https://github.com/Juanfio/Laboratorio_5/blob/master/Practica%201%20-%20Microscop%C3%ADa%20de%20Fuerza%20At%C3%B3mica/Simulacion/Simulaci%C3%B3n%20PI.ipynb
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
#import random as rm
#import math
import sys
import os
from matplotlib import rc
import Grillas as gr

path = os.path.dirname(os.path.realpath('__file__')) # Encuentra la carpeta donde está el archivo.
sys.path.append(path)

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

plt.close('all')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Configuración de las leyendas de los gráficos:
TitleSize=20
AxisLabelSize=15
LegendSize=20
NumberSize=15

#%%

grilla

lado = 50 # en nanómetros


#%%

setpoint = 110 

e_t = []
T_loop = []

pixeles = 450
total = 700 # Tiempo total en recorrer cada linea.
tiempo_por_pixel = total/pixeles
respuesta_lazo = 0.1 # Representa el tiempo que le toma al lazo corregir. Tiene que ser menor que el tiempo por pixel.

## ------------------ ** ------------------ ##    
# De esta manera el lazo logra corregirse 2 veces en cada posición.
# Cantidad de correcciones esta dada por: a) tiempo que estoy en cada pixel, b) tiempo de respuesta del lazo.
# En este caso como el tiempo que esta en cada pixel es mayor al tiempo de respuesta del lazo, logra corregir la altura mas de 
# una vez antes de cambiar de posición.
N = int(tiempo_por_pixel/respuesta_lazo)

## ------------------ ** ------------------ ##    
# Condiciones iniciales.
distancia_canti_muestra = setpoint
foto_scaneada = np.eye(40)
K_p = 1.96
K_i = 0.76
t_loop = 0

for i in range (len(grilla)):
    for j in range (len(grilla)):
        distancia_canti_muestra = distancia_canti_muestra - grilla[i][j]
        for _ in range (N):
            e_t.append (setpoint - distancia_canti_muestra) 
            T_loop.append (t_loop)
            e_t_i = sp.integrate.simps (e_t,T_loop)
            e_t_p = setpoint - distancia_canti_muestra
            distancia_canti_muestra = distancia_canti_muestra + K_p * e_t_p + K_i * e_t_i
            t_loop = t_loop + respuesta_lazo
        foto_scaneada[i][j] = distancia_canti_muestra
            
## ------------------ ** ------------------ ##    
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
