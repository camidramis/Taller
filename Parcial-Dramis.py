#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:24:08 2023

@author: clinux01
"""

#Primer Parcial
#Alumna: Camila Dramis
#LU 535/23
#Carrera: Cs. de Datos

#Ejercicio 1
#1)a.
def Fibonacci(n):
    fib = [0,1]
    for i in range(1,n):
        a=fib[i-1]+fib[i]
        fib.append(a)
    #print(fib)
    return fib[n]
Fibonacci(9)     

#Esta es la funcion que armamos en clase:
def fibonacci(n,n0=0,n1=1):
    if n == 0:
        return n0
    if n == 1:
        return n1
    return fibonacci(n-1,n0,n1) + fibonacci(n-2,n0,n1)
#fibonacci(3,n0=0,n1=1)


#1)b.
def Fibonaccer(n):
    r=n%36
    return Fibonacci(r)+1
#Fibonaccer(6)


#2)
def Perfectos(n):
    perf=[]
    for k in range(1,n):
        divisores=[]
        if k==1:
            perf.append(k)
        for i in range(1,k):
            if k%i==0:
                divisores.append(i)
        if sum(divisores)==k:
            perf.append(k)
    return perf
#Perfectos(497)


#Ejercicio 2
import numpy as np
import matplotlib.pyplot as plt

#1)a.
def borracho(n):
    posicion=0
    for i in range (1,n):
        paso=np.random.binomial(1,.5)
        if paso==1:
            posicion=posicion+1
        if paso==0:
            posicion=posicion-1
    return posicion
#borracho(50)
    

#1)b.
def borracho_promedio(n,k):
    l=[]
    for i in range (0,k+1):
        dist=abs(borracho(n))
        l.append(dist)
    return sum(l)/k
#borracho_promedio(50,6)


#1)c.
x=[(10**i) for i in range(1,7)]
y=[(borracho_promedio(j,10)) for j in x]

plt.plot(x,y)

#Se parece a una raiz!!!