from graphics import *
from random import randint
from Utility.getOption import getOption
import time

window = GraphWin("Mystery Program", 800, 800, False)

print("Select 3 points on the graph.")

#point1 = window.getMouse()
point1 = Point(200,200)
window.plot(point1.x, point1.y, 'red')
window.update()

#point2 = window.getMouse()
point2 = Point(400,600)
window.plot(point2.x, point2.y, 'red')
window.update()

#point3 = window.getMouse()
point3 = Point(200,600)
window.plot(point3.x, point3.y, 'red')
window.update()

#point4 = window.getMouse()
point4 = Point(400,200)
window.plot(point4.x, point4.y, 'red')
window.update()


iterations = int(getOption(0, 1000000))
curPoint = None
randomPoint = Point(randint(-10000,10000),randint(-10000, 10000))
points = []
color = None

start = time.time()
for x in range(iterations):
    rand = randint(0,3)
    if rand == 0:
        curPoint = point1
        color = 'red'
    elif rand == 1:
        curPoint = point2
        color = 'green'
    elif rand == 2:
        curPoint = point3
        color = 'blue'
    else:
        curPoint = point4
        color = 'black'

    randomPoint = Point((randomPoint.x + curPoint.x)/2, (randomPoint.y + curPoint.y)/2)
    points.append((randomPoint, color))
print(time.time() - start)

start = time.time()
for point in points:
    window.plot(point[0].x, point[0].y, point[1])
window.update()
print(time.time() - start)

window.getMouse()
window.close()
