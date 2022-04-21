from bokeh.plotting import figure, output_file, show
from random import randint
from math import cos

N = 5000 # количество генерируемых точек
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

output_file('math.html')

p = figure(
    title = 'MK-method',
    x_axis_label = 'X axis',
    y_axis_label = 'Y axis'
)

p.line(X, Y, legend='cos(x)', line_width=1.5)
p.circle(xgr, ygr, legend='below', size=0.5, color='green')
p.circle(xre, yre, legend='above', size=0.5, color='red')

show(p)
