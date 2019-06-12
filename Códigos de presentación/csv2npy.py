import numpy as np

path  = '/home/tom/Escritorio/AFM/Día 4/Curvas de fuerza/'
path2 = '/home/tom/Escritorio/AFM/Día 4/Curvas de fuerza/NPY/'

materiales = ['mica', 'pdms', 'vidrio', 'plastico']

for mat in materiales:
    for i in range(1, 10):
        med = str(i)

        FILE_ida    = path + mat + '_ida_' + med + '.csv'
        FILE_vuelta = path + mat + '_vuelta_' + med + '.csv'
	    # Paso los .csv a .npy
        data_ida    = np.genfromtxt(FILE_ida, delimiter=';')
        data_vuelta = np.genfromtxt(FILE_vuelta, delimiter=';')

        np.save(path2 + mat + '_ida_' + med, data_ida)
        np.save(path2 + mat + '_vuelta_' + med, data_vuelta)
