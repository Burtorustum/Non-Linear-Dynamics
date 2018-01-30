from graphics import *
from random import randint
from Utility.getOption import getOption
from math import sin, cos, pi
import time

window = GraphWin("Polygons", 800, 800, False)
window.update()
x = []
y = []
vertices = (x, y)

for n in range(5):
    x.append(350 * cos(2*pi*n/5) + 400)
    y.append(350 * sin(2*pi*n/5) + 400)

for n in range(5):
    window.plot(x[n], y[n], 'red')

window.update()
window.getMouse()
window.close()
