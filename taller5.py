#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:33:52 2023

@author: clinux01
"""

#Clase 5
#Interpolacion / Polinomio de Lagrange

#Vamos primero con los polinomios base

def polinomioLagrange(x_eval,list_x,list_y):
    coef=[]
    for i in range(len(list_x)):
        prod_1=1
        prod_2=1
        #lista = [(x_eval-list_x[j])/(list_x[i]-list_x[j]) for j in range(len(lista_x))]
        for j in range(len(list_x)):
            if i!=j:
                prod_1=prod_1*(x_eval-list_x[j])
                prod_2=prod_2*(list_x[i]-list_x[j])
        coef.append(prod_1/prod_2)
    p=list(list_y[i]*coef[i] for i in range(len(list_y)))
    return sum(p)

nodos=[8,9,14,17,18,19,20.5,21.5,23,24,25,26]
valores=[265,285,346,417,438,495,524,540,643,693,744,780]
polinomioLagrange(x_eval,nodos,valores)

x_s=np.linspace(8,27,100)
y_s=polinomioLagrange(x_s,nodos,valores)

plt.plot(x_s,y_s,'-.g')



#mat=np.array([[8,9,14,17,18,19,20.5,21.5,23,24,25,26],[265,285,346,417,438,495,524,540,643,693,744,780]])
#print (nodos)
#polinomioLagrange(8,26,nodos[0],nodos[1])


#Graficar: evaluamos Xi vs Yi:

#Algoritmo de Euclides
def mcd(a,b):
    