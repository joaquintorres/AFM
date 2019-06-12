import numpy as np
import matplotlib.pyplot as plt

path = '/home/tom/Escritorio/AFM/Día 4/Curvas de fuerza/'

material = 'vidrio'
mediciones = 9
saltos = np.zeros(mediciones)

for i in range(1, mediciones+1):
    medicion = str(i)
    FILE_vuelta = path + material + '_vuelta_' + medicion + '.csv'
    data_vuelta = np.genfromtxt(FILE_vuelta, delimiter=';')
    
    z_vuelta = data_vuelta[0,:] # En nanómetros
    F_vuelta = data_vuelta[1,:]*(10**9) # En nanonewtons
    
    F_avg = np.mean(F_vuelta[:100])
    F_min = np.min(F_vuelta)
    
    salto = F_avg - F_min
    salto = round(salto, 2)
    
    saltos[i-1] = salto

print(saltos)
print(np.mean(saltos))
