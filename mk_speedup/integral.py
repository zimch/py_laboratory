from math import cos, sin, exp
from numpy.random import randint
import time
from numba import njit


N = int(input('количество генерируемых точек: ')) # количество генерируемых точек
xmin, xmax = 0, 1
ymin, ymax = 0, 1
S = (xmax - xmin) * (ymax - ymin)
xgr, ygr = [], []
xre, yre = [], []

@njit
def mk():
    counter = []
    for i in range(N):
        xg, yg = randint(1, 1000) / 1000, randint(1, 1000) / 1000
        if yg <= cos(xg):
            counter.append(1)
        else:
            counter.append(0)
        
    percent = counter.count(1) / N
    return S * percent, counter
    
start = time.time()
integral = mk()
print(time.time() - start)
print('приближенное значение интеграла:', integral[0])
