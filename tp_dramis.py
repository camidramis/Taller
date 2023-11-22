# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:12:20 2023

@author: Usuario
"""

#Trabajo Práctico: Billar Elíptico con Obstáculo
#2do Cuatrimestre 2023

#Alumna: Camila Dramis
#LU: 535/23

#En este TP deben hacer simulaciones numéricas sobre un billar con borde
#elíptico y un obstáculo cuadrado centrado en la elipse.

import matplotlib.pyplot as plt
import numpy as np

def derivar(u,g,h):
    return (g(u+h)-g(u-h))/(2*h)

def metNewton(xi,f,kmax):
    k=0
    while k<kmax:
        if derivar(xi,f,0.001)!=0:
            xf=xi-f(xi)/derivar(xi,f,0.001)
            xi=xf
            k=k+1
        else:
            return xf, k
    return xf, k

#Graficar la elipse:
theta=np.linspace(-10, 10, 1000)
a,b=2,3
x=a*np.cos(theta)
y=b*np.sin(theta)

#Tengo que definir los focos dentro de la elpse
