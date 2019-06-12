import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[scaled=0.85]{librebaskerville}, \usepackage[lite]{mtpro2}, \usepackage[unit-mode=text]{siunitx}, \sisetup{math-rm=\mathnormal}')
plt.rc('font', family='serif')
plt.rc('axes', grid=True, labelsize=16, lw=1.8)
plt.rc('grid', c='d3d3d3', ls='--', lw=1.8)
plt.rc(['xtick', 'ytick'], direction='in', labelsize=16)
plt.rc(['xtick.major', 'ytick.major'], size=7, width=1.8)
plt.rc('legend', fontsize=14)

##########################################################################
path = '/home/tom/Escritorio/AFM/Día 4/Curvas de fuerza/'

material = 'mica'
medicion = '1' # El número de la medición

FILE_ida    = path + material + '_ida_' + medicion + '.csv'
FILE_vuelta = path + material + '_vuelta_' + medicion + '.csv'

# Paso los .csv a .npy
data_ida    = np.genfromtxt(FILE_ida, delimiter=';')
data_vuelta = np.genfromtxt(FILE_vuelta, delimiter=';')

z_ida = data_ida[0,:]*(10**6) # En nanómetros
F_ida = data_ida[1,:]*(10**9) # En nanonewtons

z_vuelta = data_vuelta[0,:]*(10**6) # En nanómetros
F_vuelta = data_vuelta[1,:]*(10**9) # En nanonewtons

##########################################################################
fig, ax = plt.subplots()

ida,    = ax.plot(z_ida, F_ida, c='blue', ls='--', label=r'acercamiento del cantilever', lw=4, zorder=3)
vuelta, = ax.plot(z_vuelta, F_vuelta, c='red', label=r"retracci\'{o}n del cantilever", lw=4)

ax.text(-0.575, 6.5, r"fuerza de", ha='center', rotation=90, fontsize=14)
ax.text(-0.54, 6.5, r"arranque", ha='center', rotation=90, fontsize=14)
ax.text(-1.152, 14.2, r"lejos de la muestra", fontsize=14)
ax.text(-0.27, 47, r"cerca de la muestra", ha='right', rotation=70, fontsize=14)

ax.annotate('', xy=(-0.515, 12.8), xytext=(-0.515, -7.4), arrowprops=dict(arrowstyle='<->', connectionstyle='arc3', lw=1.8))
ax.annotate('', xy=(-0.85, 14.7), xytext=(-0.65, 14.7), arrowprops=dict(arrowstyle='<-', connectionstyle='arc3', color='blue', lw=2.5))
ax.annotate('', xy=(-0.39, 24.5), xytext=(-0.43, 15.3), arrowprops=dict(arrowstyle='<-', connectionstyle='arc3', color='red', lw=2.5))

ax.annotate(r"trabajo" "\n" r"de adhesi\'{o}n", xy=(-0.47, 6.6), xytext=(-0.35, -2.5), ha='center', arrowprops=dict(arrowstyle='<-', connectionstyle='arc3, rad=0.3', color='black', lw=1.8), fontsize=14)

plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.05, 0.02), loc='lower left').get_frame().set_lw(1.8)

### Zoom:
axins = zoomed_inset_axes(ax, 10, bbox_to_anchor=(0.08, 0.95), loc='upper left', bbox_transform=ax.transAxes)

axins.plot(z_ida, F_ida, c='blue', ls='--', lw=4)
axins.plot(z_vuelta, F_vuelta, c='red', lw=4)

axins.annotate('', xy=(-0.382, 11.65), xytext=(-0.382, 12.54), arrowprops=dict(arrowstyle='<->', connectionstyle='arc3', lw=1.8))
axins.text(-0.365, 12.05, r"snap-in", ha='right', fontsize=17)

x1, x2, y1, y2 = -0.425, -0.36, 11.5, 13.5
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

plt.xticks(visible=False)
plt.yticks(visible=True)

mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5", lw=1.5, zorder=4)

plt.draw()

plt.tight_layout(pad=0.3)
plt.show()
