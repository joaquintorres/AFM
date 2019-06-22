#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:23:09 2019

@author: muriel
"""
from __future__ import division
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse

matriz = np.loadtxt('/home/muriel/Documents/Laboratorio_5/AFM/Datos_clase_2/prueba_1')

T = matriz

K = (9000,1000,0)

fig, ax = plt.subplots()

plt.subplots_adjust(top=0.94, bottom=0.04, left=0.01, right=1.07, hspace=0.30, wspace=0.30)

ax.set_title(' $K_P = %.1f$, $K_I = %.1f$, $K_D = %.1f$' % K )


image = [0]

image = ax.imshow(T, cmap=plt.cm.gray)

# Calculo los valores mínimo y máximo para todas las matrices, así delimito bien el rango del colorbar
vmin = image.get_array().min()
vmax = image.get_array().max()
norm = colors.Normalize(vmin=vmin, vmax=vmax)

image.set_norm(norm)

# Escala de grises para la altura z
cbar = fig.colorbar(image, ax=ax)
cbar.set_label(r'altura $z$ (nm)', y=0.5, fontsize=20) # Usar la lista T en el imshow
#cbar.set_label(r'fuerza $F$ (nN)', y=0.5, fontsize=20) # Usar la lista D en el imshow

plt.show()

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = '/home/muriel/Documents/Laboratorio_5/AFM/Datos_clase_2/prueba_1')
#args = vars(ap.parse_args())

circles = cv2.HoughCircles(T, cv2.HOUGH_GRADIENT, 1.2, 100)
