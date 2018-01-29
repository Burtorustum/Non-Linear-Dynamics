from graphics import *
from random import randint
from Utility.getOption import getOption
import time

window = GraphWin("Mystery Program", 800, 800, False)
endPoints = []
points = []
lastRand = None
colors = ['black', 'red', 'blue', 'green', 'purple', 'pink', 'brown', 'teal', 'orange']
curPoint = None

numPoints = int(input("Input the number of points you want to choose. "))
print("Choose your points!")
for x in range(numPoints):
    endPoints.append(window.getMouse())
    window.plot(endPoints[-1].x,endPoints[-1].y, 'red')
    window.update()

print("Choose your number of iterations.")
iterations = int(getOption(0, 100000))
randomPoint = Point(randint(-10000, 10000), randint(-10000, 10000))

inverse = True if input("Would you like to plot the inverse fractal? y/n ").lower() == 'y' else False

start = time.time()
for x in range(iterations):
    rand = randint(1,numPoints) - 1
    if inverse:
        if rand == lastRand:
            rand += 1
            if rand == numPoints:
                rand = 0
        lastRand = rand
    curPoint = endPoints[rand]
    randomPoint = Point((randomPoint.x + curPoint.x)/2, (randomPoint.y + curPoint.y)/2)
    points.append((randomPoint, colors[rand]))
print(time.time() - start)

start = time.time()
for point in points:
    window.plot(point[0].x, point[0].y, point[1])
window.update()
print(time.time() - start)

window.getMouse()
window.close()
