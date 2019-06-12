import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[scaled=0.85]{librebaskerville}, \usepackage[lite]{mtpro2}, \usepackage[unit-mode=text]{siunitx}, \sisetup{math-rm=\mathnormal}')
plt.rc('font', family='serif')
plt.rc('axes', grid=True, labelsize=16, titlesize=18, titlepad=10, lw=1.8)
plt.rc('grid', c='d3d3d3', ls='--', lw=1.8)
plt.rc(['xtick', 'ytick'], direction='in', labelsize=16)
plt.rc(['xtick.major', 'ytick.major'], size=7, width=1.8)
plt.rc('legend', fontsize=14)

##########################################################################
path = '/home/tom/Escritorio/AFM/Día 4/Curvas de fuerza/NPY/'

mica_ida_1    = np.load(path + 'mica_ida_3' + '.npy')
mica_vuelta_1 = np.load(path + 'mica_vuelta_3' + '.npy')

mica_ida_2    = np.load(path + 'mica_ida_5' + '.npy')
mica_vuelta_2 = np.load(path + 'mica_vuelta_5' + '.npy')

pdms_ida_1    = np.load(path + 'pdms_ida_1' + '.npy')
pdms_vuelta_1 = np.load(path + 'pdms_vuelta_1' + '.npy')

pdms_ida_2    = np.load(path + 'pdms_ida_2' + '.npy')
pdms_vuelta_2 = np.load(path + 'pdms_vuelta_2' + '.npy')

vidrio_ida_1    = np.load(path + 'vidrio_ida_5' + '.npy')
vidrio_vuelta_1 = np.load(path + 'vidrio_vuelta_5' + '.npy')

vidrio_ida_2    = np.load(path + 'vidrio_ida_7' + '.npy')
vidrio_vuelta_2 = np.load(path + 'vidrio_vuelta_7' + '.npy')

##########################################################################
plt.figure(1)

plt.subplots_adjust(top=0.95, bottom=0.08, left=0.04, right=0.995, hspace=0.35, wspace=0.3)

LW = 3.5

plt.subplot(231)

ida,    = plt.plot(mica_ida_1[0,:]*(10**6), mica_ida_1[1,:]*(10**9), c='blue', ls='--', label=r'acercamiento del cantilever', lw=LW, zorder=3)
vuelta, = plt.plot(mica_vuelta_1[0,:]*(10**6), mica_vuelta_1[1,:]*(10**9), c='red', label=r"retracci\'{o}n del cantilever", lw=LW)

plt.title('(a) Mica')
plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.01, 1), loc='upper left').get_frame().set_lw(1.8)

plt.subplot(232)

ida,    = plt.plot(pdms_ida_1[0,:]*(10**6), pdms_ida_1[1,:]*(10**9), c='blue', ls='--', label=r'acercamiento del cantilever', lw=LW, zorder=3)
vuelta, = plt.plot(pdms_vuelta_1[0,:]*(10**6), pdms_vuelta_1[1,:]*(10**9), c='red', label=r"retracci\'{o}n del cantilever", lw=LW)

plt.title('(c) PDMS')
plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.01, 1), loc='upper left').get_frame().set_lw(1.8)

plt.subplot(233)

ida,    = plt.plot(vidrio_ida_1[0,:]*(10**6), vidrio_ida_1[1,:]*(10**9), c='blue', ls='--', label=r'acercamiento del cantilever', lw=LW, zorder=3)
vuelta, = plt.plot(vidrio_vuelta_1[0,:]*(10**6), vidrio_vuelta_1[1,:]*(10**9), c='red', label=r"retracci\'{o}n del cantilever", lw=LW)

plt.title('(e) Vidrio')
plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.01, 1), loc='upper left').get_frame().set_lw(1.8)

plt.subplot(234)

ida,    = plt.plot(mica_ida_2[0,:]*(10**6), mica_ida_2[1,:]*(10**9), c='blue', ls='--', label=r'acercamiento del cantilever', lw=LW, zorder=3)
vuelta, = plt.plot(mica_vuelta_2[0,:]*(10**6), mica_vuelta_2[1,:]*(10**9), c='red', label=r"retracci\'{o}n del cantilever", lw=LW)

plt.title('(b) Mica')
plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.01, 1), loc='upper left').get_frame().set_lw(1.8)

plt.subplot(235)

ida,    = plt.plot(pdms_ida_2[0,:]*(10**6), pdms_ida_2[1,:]*(10**9), c='blue', ls='--', label=r'acercamiento del cantilever', lw=LW, zorder=3)
vuelta, = plt.plot(pdms_vuelta_2[0,:]*(10**6), pdms_vuelta_2[1,:]*(10**9), c='red', label=r"retracci\'{o}n del cantilever", lw=LW)

plt.title('(d) PDMS')
plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.01, 1), loc='upper left').get_frame().set_lw(1.8)

plt.subplot(236)

ida,    = plt.plot(vidrio_ida_2[0,:]*(10**6), vidrio_ida_2[1,:]*(10**9), c='blue', ls='--', label=r'acercamiento del cantilever', lw=LW, zorder=3)
vuelta, = plt.plot(vidrio_vuelta_2[0,:]*(10**6), vidrio_vuelta_2[1,:]*(10**9), c='red', label=r"retracci\'{o}n del cantilever", lw=LW)

plt.title('(f) Vidrio')
plt.xlabel(r'distancia~$z$ ($\si{\micro\meter}$)')
plt.ylabel(r'fuerza~$F$ ($\si{\nano\newton}$)')
plt.legend(handles=[ida, vuelta], bbox_to_anchor=(0.01, 1), loc='upper left').get_frame().set_lw(1.8)

plt.show()
