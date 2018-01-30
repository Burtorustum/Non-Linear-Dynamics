from graphics import *
from random import randint
from Utility.getOption import getOption
from math import sqrt
import time

window = GraphWin("Square Circles", 800, 800, False)
window.update()
points = []
lastRand = Point(0,0)
randPoint = Point(0,0)
curPoint = Point(randint(0,800),randint(0,800))

vertices = [Point(0,0), Point(800, 0), Point(800, 800), Point(0,800)]

iterations = 1000000

for x in range(iterations):
    randPoint = vertices[randint(0,3)]
    while randPoint.x != lastRand.x and randPoint.y != lastRand.y:
        randPoint = vertices[randint(0,3)]

    curPoint = Point((randPoint.x + curPoint.x)/2, (randPoint.y + curPoint.y)/2)
    lastRand = randPoint
    points.append((curPoint, 'black'))
    #print(curPoint)

for point in points:
    window.plot(point[0].x, point[0].y, point[1])
window.update()
window.getMouse()
window.close()
