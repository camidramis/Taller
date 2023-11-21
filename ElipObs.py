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
trand = np.random.uniform(0, 2*np.pi)
o = np.array([np.random.uniform(-a,a)*np.cos(trand), np.random.uniform(-b,b)*np.sin(trand)])




#Linea1

#-b<y<b  x=0

ys = np.linspace (-b,b, 100)
xs = 0*np.ones(100)

plt.plot(xs, ys)

#impacto con la Linea


def reflexion(o, unit_v):
    
    t1 = (0-o[0])/unit_v[0]

    if t1*unit_v[1]+o[1] < b and t1*unit_v[1]+o[1] > -b:
        pimpacto = t1*unit_v + o 
        normal = np.array([1,0])
    else:
        E2 = lambda x: (x[0]**2)/(a**2) + (x[1]**2)/(b**2) - 1
        h = lambda t: E2(t*unit_v + o)
        t = NRroots(h, 50, 800)
        pimpacto = t*unit_v + o
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

k = 1

plt.axis("equal")
plt.title(f"{k} Colisiones en Elipse a={a} b={b}")
plt.plot(x, y)
plt.quiver(o[0], o[1], unit_v[0], unit_v[1], width = 0.004)
#plt.plot(pimpacto[0], pimpacto[1], "o")

plt.plot(colisiones(k, o, unit_v)[0], colisiones(k, o, unit_v)[1])
plt.plot([f1, f2], [0, 0], "x")
plt.plot(o[0], o[1], 'o')

plt.show()