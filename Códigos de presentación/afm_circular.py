from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[scaled=0.85]{librebaskerville}, \usepackage[lite]{mtpro2}')
plt.rc('font', family='serif')
plt.rc('axes', titlesize=20, titlepad=12)
plt.rc(['xtick', 'ytick'], labelsize=18)

#####################################################################################################
# ARMO LA GRILLA

h = 100 # Altura en nm
dim = 200 # Cantidad de píxeles para un "pitch"
A = np.random.rand(dim,dim)*3 # Este es el "pitch" patrón, después lo voy a concatenar ya que la grilla es periódica.
                              # El *3 es debido al "3% height accuracy" del fabricante de la grilla

# Fabrico el "pitch" circular:
for i in range(0, dim):
    for j in range(0, dim):
        if np.sqrt((i-99)**2 + (j-99)**2) <= 66: # Ecuación del círculo
            A[i,j] = A[i,j] + h # Si está dentro del círculo sumo h, sino que quede con un nro. random entre 0 y 3

p = 2 # La grilla va a ser de "p x p" pitch's
R = np.concatenate((A,) * p) # Primera concatenación: un "pitch" debajo del otro
G = np.concatenate((R,) * p, axis=1) # Al "rectangulo" R lo concateno uno al lado del otro: obtengo la grilla circular G

#####################################################################################################
# SIMULO EL LAZO DE CONTROL PID

px = dim*p # Los píxeles (elementos de matriz) de una línea de grilla, o sea, la matriz G es de px x px

k  = 0.6 # Constante del resorte (cantilever "lineal")
SP = 50  # Setpoint en nN

# Constantes Kp, Ki y Kd (en ese orden) del controlador PID. Las letras las usamos luego al plotear las figuras
K = [
    ('a', 0, 0, 0),
    ('b', 0.10, 0.00, 0),
    ('c', 0.20, 0.10, 0),
    ('d', 1.90, 1.70, 0),
    ('e', 1.70, 0.80, 0),
    ('f', 1.70, 0.80, 0.30),
]

rows = 2
cols = 3
N = rows * cols

T = [np.zeros((px, px)),] * N
T[0] = G

D = [np.zeros((px, px)),] * N
D[0] = SP * np.ones((px, px))

for n in range(1, N):
    Kp = K[n][1]
    Ki = K[n][2]
    Kd = K[n][3]

    f = np.zeros((px, px)) # Matriz de mediciones de fuerza
    u = np.zeros((px, px)) # Matriz de correcciones dada una desviación
    z = np.zeros((px, px)) # Matriz de alturas (topografía)
    U = np.zeros(px) # Para cada línea, voy sumando las correcciones del lazo a medida que barro
    Z = np.zeros(px) # Es parecida a U en su construcción sólo que cambia el signo: si hay una depresión en la topografía (altura 
                     # "NEGATIVA"), el lazo habrá corregido con una fuerza POSITIVA (hacia arriba tal que deflecte el cantilever).

    for i in range (0, px): # Fila i (de arriba hacia abajo)
        for j in range(0, px): # Para la fila i, barro en j (de izquierda a derecha)
            f[i,j] = k * (G[i,j] - G[0,0]) + U[i] # Mido la fuerza en la posición (i,j). Al setpoint le sumo cuánto comprime
                                                  # la muestra al resorte-cantilever y las correcciones que va haciendo el lazo

            u[i,j] = Kp * (-1*f[i,j]) + Ki * (np.sum(-1*f[i,:j])) + Kd * (-1*f[i,j] - (-1)*f[i,j-1]) # Para esa desviación, el lazo PID corrije
            U[i] = U[i] + u[i,j] # Voy sumando las correcciones del lazo para sumarlas a la mediciones de fuerza f: no sólo
                                 # la topografía contribuye a la fuerza medida
            Z[i] = Z[i] - u[i,j] # Para cada linea sumo las correciones (con signo corregido) hechas hasta los primeros j píxeles barridos
            z[i,j] = Z[i]/k # Hasta ahora todas las mediciones eran de fuerza, como lo modelo con un resorte paso la fuerza a distancia
    
    T[n] = z
    D[n] = f + SP * np.ones((px, px))

#####################################################################################################
# PLOTEO LA GRILLA Y LAS TOPOGRAFÍAS

fig, axs = plt.subplots(rows, cols)

plt.subplots_adjust(top=0.94, bottom=0.04, left=0.01, right=1.07, hspace=0.30, wspace=0.30)

for i, ax in enumerate(axs.flat):
    ax.set_title('(%s) $K_P = %.1f$, $K_I = %.1f$, $K_D = %.1f$' % K[i])

axs[0,0].set_title(r"(a) Grilla de calibraci\'{o}n") # Para la topografía T
#axs[0,0].set_title(r"(a) Controlador ``perfecto''") # Para la deflexión D

images = [0,] * N

for i in range(rows*cols):
    images[i] = axs.flat[i].imshow(T[i], cmap=plt.cm.gray)

# Calculo los valores mínimo y máximo para todas las matrices, así delimito bien el rango del colorbar
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

# Escala de grises para la altura z
cbar = fig.colorbar(images[0], ax=axs, location='right')
cbar.set_label(r'altura $z$ (nm)', y=0.5, fontsize=20) # Usar la lista T en el imshow
#cbar.set_label(r'fuerza $F$ (nN)', y=0.5, fontsize=20) # Usar la lista D en el imshow

plt.show()
