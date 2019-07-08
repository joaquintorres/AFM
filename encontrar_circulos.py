# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:48:15 2019

@author: julie
"""
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2



img = cv2.imread(r'C:\Users\julie\OneDrive\Documentos\FCEyN\Laboratorio 5\AFM\Dia 2\Dia 2\Dia2-Grupo400031_zaxis.PNG',0)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR) 
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=50)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
     # draw the outer circle
     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
     # draw the center of the circle
     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',cimg)


centro = [(n,m) for n in circles[0,:][:,0] for m in circles[0,:][:,1]]

centro = np.array(list(zip(circles[0,:][:,0],circles[0,:][:,1])))

radios =round(np.mean(circles[0,:][:,2]),0)

#### Defino la grilla ###

h = 100 # Altura en nm

dimx = np.shape(img)[0] 
dimy = np.shape(img)[1]

grilla = np.random.rand(dimx, dimy)*3 +100 # El *3 es debido al "3% height accuracy" del fabricante de la grilla
                             
for n in centro:
    for i in range(0, dimx):
        for j in range(0, dimy):
            if np.sqrt((j-n[0])**2 + (i-n[1])**2) <= radios: # Ecuación del círculo
                grilla[i,j] = grilla[i,j] - h # Si está dentro del círculo sumo h, sino que quede con un nro. random entre 0 y 3

# redefino el tamaño de la imagen para que solo haya circulos

maxcentro_x = min([max(centro[:,1]) + 40,dimx])
maxcentro_y = min([max(centro[:,0]) + 40,dimy])               
mincentro_x = max([min(centro[:,1]) - 40,0])
mincentro_y = max([min(centro[:,0]) - 40,0])

grilla = grilla[mincentro_x:maxcentro_x,mincentro_y:maxcentro_y]
img = img[mincentro_x:maxcentro_x,mincentro_y:maxcentro_y]
cimg = cimg[mincentro_x:maxcentro_x,mincentro_y:maxcentro_y]
cv2.imshow('detected circles',cimg)

fig, ax = plt.subplots()

plt.subplots_adjust(top=0.94, bottom=0.04, left=0.01, right=1.07, hspace=0.30, wspace=0.30)

#axs[0,0].set_title(r"(a) Controlador ``perfecto''") # Para la deflexión D

image = ax.imshow(grilla, cmap=plt.cm.gray)

# Calculo los valores mínimo y máximo para todas las matrices, así delimito bien el rango del colorbar
vmin = image.get_array().min()
vmax = image.get_array().max()
norm = colors.Normalize(vmin=vmin, vmax=vmax)


image.set_norm(norm)

# Escala de grises para la altura z
cbar = fig.colorbar(image)
cbar.set_label(r'altura $z$ (nm)', y=0.5, fontsize=20) # Usar la lista T en el imshow
#cbar.set_label(r'fuerza $F$ (nN)', y=0.5, fontsize=20) # Usar la lista D en el imshow


##### LA RESTAAAAAAA #########
resta = img - grilla

fig, ax = plt.subplots()

plt.subplots_adjust(top=0.94, bottom=0.04, left=0.01, right=1.07, hspace=0.30, wspace=0.30)

#axs[0,0].set_title(r"(a) Controlador ``perfecto''") # Para la deflexión D

image = ax.imshow(resta, cmap=plt.cm.gray)

# Calculo los valores mínimo y máximo para todas las matrices, así delimito bien el rango del colorbar
vmin = image.get_array().min()
vmax = image.get_array().max()
norm = colors.Normalize(vmin=vmin, vmax=vmax)


image.set_norm(norm)

# Escala de grises para la altura z
cbar = fig.colorbar(image)
cbar.set_label(r'altura $z$ (nm)', y=0.5, fontsize=20) # Usar la lista T en el imshow
#cbar.set_label(r'fuerza $F$ (nN)', y=0.5, fontsize=20) # Usar la lista D en el imshow



