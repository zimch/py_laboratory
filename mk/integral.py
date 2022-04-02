import matplotlib.pyplot as plt
from math import cos
from random import randint

N = int(input('количество генерируемых точек: ')) # количество генерируемых точек
# a, b = 0, 1 
xmin, xmax = 0, 1
ymin, ymax = 0, 1
counter = []
S = (xmax - xmin) * (ymax - ymin)
xgr, ygr = [], []
xre, yre = [], []

def f(x):
    return cos(x)


def mk():
    for i in range(N):
        xg, yg = randint(0, 1000) / 1000, randint(0, 1000) / 1000
        if yg <= f(xg):
            counter.append(1)
            xgr.append(xg)
            ygr.append(yg)
        else:
            counter.append(0)
            xre.append(xg)
            yre.append(yg)
        
    percent = counter.count(1) / N
    return S * percent
    

integral = mk()
X = [i / 1000 for i in range(1000)]
Y = [f(i / 1000) for i in range(1000)]

plt.plot(X, Y, color='black')
plt.plot(xgr, ygr, 'go', markersize=0.8)
plt.plot(xre, yre, 'ro', markersize=0.8)

plt.show()
print('приближенное значение интеграла:', integral)