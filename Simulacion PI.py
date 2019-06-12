# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:49:05 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import random as rm
import math


e_t = []
T = []
dt = 1
t = 0
X = []
x = 0
paso = 0.1
setpoint = 4
K_p = 1
K_i = 0.2
N = 1000
medicion = 1000


for _ in range (medicion):
    for _ in range (N):
        val_azar = rm.uniform (-paso,paso)
        x = x + val_azar
    e_t.append (setpoint - x)
    T.append (t)
    e_t_i = sp.integrate.simps (e_t,T)
    e_t_1 = setpoint - x
    t = t + dt
    x = x + K_p * e_t_1 + K_i * e_t_i
    X.append (x)
    

plt.grid()
plt.xlabel ("Tiempo")
plt.ylabel ("X")
plt.plot (T,X)
plt.show ()
