#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:06:25 2023

@author: clinux01
"""

#Raices por Newton-Raphson
der = lambda f, x, h: (f(x+h)-f(x-h))/(2*h)

def NRroots(f, x, k):
    for i in range(k):
        if der(f, x, 0.001) != 0:
            x1 = x - f(x)/(der(f, x, 0.001))
            x = x1
        else:
            return x1
    return x

import matplotlib.pyplot as plt
import numpy as np

#random unit vector cordinates
v = np.random.uniform(-1, 1, size=2)
unit_v = v/((v[0]**2 + v[1]**2)**.5)


#Drawing elipse
a, b = 7, 5

s = np.linspace(-6, 6, 1000)

x = a*np.cos(s)
y = b*np.sin(s)

#Focos elipse
f1 = -abs((a**2 - b**2))**.5
f2 = abs((a**2 - b**2))**.5

#random point in the elipse
randt = np.random.uniform(0, 2*np.pi )
o = np.array([np.random.uniform(-a,a)*np.cos(randt), np.random.uniform(-b,b)*np.sin(randt)])

#Vertice  h = altura cuadrilatero   ::: b = base
#     P1-------P2
#      |        |
#      |        |
#     P3-------P4
height = 4
base = 4
P1 = np.array([-2, 2])
P2 = np.array([P1[0]+base, P1[1]])
P3 = np.array([P1[0], P1[1]-height])
P4 = np.array([P1[0]+base, P1[1]-height])


def colElips(o, unit_v):
  E2 = lambda x: (x[0]**2)/(a**2) + (x[1]**2)/(b**2) - 1
  h = lambda t: E2(t*unit_v + o)
  t = NRroots(h, 50, 800)
  pimpacto = t*unit_v + o
  return pimpacto

def colLinx(o, unit_v, y):
  pimpacto = ((y[1]-o[1])/unit_v[1])*unit_v + o
  return pimpacto

def colLiny(o, unit_v, y):
  pimpacto = ((y[0]-o[0])/unit_v[0])*unit_v + o
  return pimpacto

def reflexion(o, unit_v):
    
    #Particion elipse
    #  IS   MS   DS
    #  DM   ###  IM
    #  II   MI   DI
    #
    #
    
    #Medio Superior
    if o[1] > P1[1] and o[0] > P1[0] and o[0] < P2[0]:

        if unit_v[1] < 0:
            pimpacto = colLinx(o, unit_v, P1)
    
            if pimpacto[0] < 2 and -2 < pimpacto[0]:
              normal = np.array([0,-1])
            else:
              pimpacto = colElips(o, unit_v)
              grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
              normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
    
        else:
            pimpacto = colElips(o, unit_v)
            grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
            normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)    
    
    #Izquierda Superior
    elif o[1] > P1[1] and o[0] < P1[0]:
        if v[1] < 0:
            pimpacto = colLinx(o, unit_v, P1)
            if pimpacto[0] < 2 and -2 < pimpacto[0]:
              normal = np.array([0,-1])
            else:
                pimpacto = colLiny(o, unit_v, P1)
                if pimpacto[1] < 2 and  -2 < pimpacto[1]:
                    normal = np.array([1,0])
                else:
                    pimpacto = colElips(o, unit_v)
                    grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
                    normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
    
        else:
          pimpacto = colElips(o, unit_v)
          grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
          normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
              
         
    #Derecha Superior
    elif o[1] > P1[1] and o[0] > P2[0]: 
        pimpacto = colElips(o, unit_v)
        grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
        normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)    
    
    #Izquierda Inferior
    elif o[1] < P3[1] and o[0] < P1[0]:
        pimpacto = colElips(o, unit_v)
        grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
        normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)    
       
    #Medio Inferior
    elif o[1] < P3[1] and o[0] > P1[0] and o[0] < P2[0]:    
        if unit_v[1] > 0: 
          pimpacto = colLinx(o, unit_v, P3)
          
          if pimpacto[0] < 2 and  -2 < pimpacto[0]:
            normal = np.array([0,1])
          else:
            pimpacto = colElips(o, unit_v)
            grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
            normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
        
        else:
          pimpacto = colElips(o, unit_v)
          grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
          normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
        
    #Derecha Inferior
    elif o[1] < P3[1] and o[0] > P2[0]:
        pimpacto = colElips(o, unit_v)
        grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
        normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)    
       
    #Derecha Medio
    elif o[1] > P3[1] and o[1] < P1[1] and o[0] > P2[0]:
        if unit_v[0] < 0:
          pimpacto = colLiny(o, unit_v, P2)
          if pimpacto[1] < 2 and -2 < pimpacto[1]:
            normal = np.array([-1,0])
          else:
            pimpacto = colElips(o, unit_v)
            grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
            normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
    
        else:
          pimpacto = colElips(o, unit_v)
          grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
          normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)

      
    #Izquierdo Medio
    elif o[1] > P3[1] and o[1] < P1[1] and o[0] < P1[0]:
        if unit_v[0] > 0:
          pimpacto = colLiny(o, unit_v, P1)
          if pimpacto[1] < 2 and  -2 < pimpacto[1]:
            normal = np.array([1,0])
          else:
            pimpacto = colElips(o, unit_v)
            grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
            normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
    
        else:
          pimpacto = colElips(o, unit_v)
          grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
          normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)
    
    else:
          pimpacto = colElips(o, unit_v)
          grad = lambda x: np.array([(2*x[0])/a**2, (2*x[1])/b**2])
          normal = grad(pimpacto)/((grad(pimpacto)[0]**2 + grad(pimpacto)[1]**2)**.5)

    

    #vector reflect v-2P_N(v)

    PnV = np.dot(normal, unit_v)*normal
    refl_v = unit_v - 2*PnV

    if np.dot(refl_v, normal) > 0:
        refl_v = -refl_v

    return pimpacto ,refl_v

def colisiones(k, pinicial, dinicial):
    j = 0
    lcolisionx = np.array([pinicial[0]])
    lcolisiony = np.array([pinicial[1]])
    while j <= k:
        p1 = reflexion(pinicial, dinicial)[0]
        d1 = reflexion(pinicial, dinicial)[1]
        lcolisionx = np.append(lcolisionx, p1[0])
        lcolisiony = np.append(lcolisiony, p1[1])
        pinicial = p1
        dinicial = d1
        j += 1
    return lcolisionx, lcolisiony

#Linea vertical
plt.plot( P1, P2, P3, P4) #P12
plt.plot( [P3[0], P4[0]], [P3[1], P3[1]]) #P34
k = 3

plt.axis("equal")
plt.title(f"{k} Colisiones en Elipse a={a} b={b}")
plt.plot(x, y)
plt.quiver(o[0], o[1], unit_v[0], unit_v[1], width = 0.004)
array_colisiones = colisiones(k, o , unit_v)
plt.plot(array_colisiones[0], array_colisiones[1])
plt.plot([f1, f2], [0, 0], "x")
plt.plot(o[0], o[1], 'o')

plt.show()







##Particion elipse
##  IS   MS   DS
##  DM   ###  IM
##  II   MI   DI
##
##
##Izquierda Superior
#
#if o[1] > P1[1] and o[0] < P1[0]:
#    
##Medio Superior
#
#if o[1] > P1[1] and o[0] > P1[0] and o[0] < P2[0]
#    
##Derecha Superior
#
#if o[1] > P1[1] and o[0] > P2[0]:    
#    
##Izquierda Inferior
#
#if o[1] < P3[1] and o[0] < P1[0]:
#    
##Medio Inferior
#
#if o[1] < P3[1] and o[0] > P1[0] and o[0] < P2[0]:    
#    
##Derecha Inferior
#
#if o[1] < P3[1] and o[0] > P2[0]:
#
##Derecha Medio
#
#if o[1] > P3[1] and o[1] < P1[1] and o[0] > P2[0]:
#    
##Izquierdo Medio
#
#if o[1] > P3[1] and o[1] < P1[1] and o[0] < P1[0]:
#
#













