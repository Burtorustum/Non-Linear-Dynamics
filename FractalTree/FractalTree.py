#FractalTree.py
import copy as copy
import math as math
from nld_graphics import *
from random import uniform, randrange

class FractalTree:

    def __init__(self, initialAngle, scaleFactor, window):
        if window == None:
            self.window = NLDGraphWin("Fractal Tree", 600, 600, [-5,-5,5,5])
        else:
            self.window = window
        self.initialAngleDeg = initialAngle
        self.initialAngle = math.radians(initialAngle)
        self.scaleFactor = scaleFactor
        self.startLenWinItems = len(window.items)
        self.endLenWinItems = len(window.items)

    def drawLine(self, startPoint, length, direction, color='black', width=3):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        l = Line(ogPoint, startPoint)
        l.setFill(color)
        l.setWidth(width)
        l.draw(self.window)

    def drawTreeRec(self, level, point, length, angle, animated=True, colored=True, randomLength=False, randomAngle=False, leftFactor=1, rightFactor=1, widthScaling=True, width=10, assymetricLevel=0):

        if width < 1:
            width = 1

        #Draw the branches of the tree
        if level < 2:
            self.drawLine(point, length, angle, color= ('darkgreen' if colored else 'black'), width=width)
        else:
            self.drawLine(point, length, angle, color= ('saddlebrown' if colored else 'black'), width=width)

        if animated:
            self.window.update()

        nextLength = length * self.scaleFactor * (uniform(self.scaleFactor,1) if randomLength else 1)
        nextAngle1 = angle - rightFactor*self.initialAngle+(math.radians(randrange(-int(abs(self.initialAngleDeg)),int(abs(self.initialAngleDeg)))) if randomAngle else 0)
        nextAngle2 = angle + rightFactor*self.initialAngle+(math.radians(randrange(-int(abs(self.initialAngleDeg)),int(abs(self.initialAngleDeg)))) if randomAngle else 0)

        if level != -1:
            point2 = copy.copy(point)
            self.drawTreeRec(level-1, point, nextLength, nextAngle1, width= (width-1 if widthScaling else width), animated=animated, colored=colored, randomLength=randomLength,randomAngle=randomAngle, widthScaling=widthScaling, leftFactor= (1 if assymetricLevel <= 0 else leftFactor), rightFactor= (1 if assymetricLevel <= 0 else rightFactor), assymetricLevel= (0 if assymetricLevel <= 0 else assymetricLevel-1))
            self.drawTreeRec(level-1, point2, nextLength, nextAngle2, width= (width-1 if widthScaling else width), animated=animated, colored=colored, randomLength=randomLength, randomAngle=randomAngle, widthScaling=widthScaling, leftFactor= (1 if assymetricLevel <= 0 else leftFactor), rightFactor= (1 if assymetricLevel <= 0 else rightFactor), assymetricLevel= (0 if assymetricLevel <= 0 else assymetricLevel-1))
        else:
            self.endLenWinItems = len(self.window.items)
            
    def clear(self):
        for x in reversed(range(self.startLenWinItems, self.endLenWinItems)):
            self.window.items[x] = Line(Point(-1000,-1000),Point(-1001,-1001))
        #self.window.items = []
        self.window.clear()
        self.scaleFactor = 1
        self.initialAngleDeg = 0
        self.initalAngle = 0
