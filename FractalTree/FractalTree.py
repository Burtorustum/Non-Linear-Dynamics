#FractalTree.py
import copy as copy
import math as math
from nld_graphics import *

class FractalTree:

    def __init__(self, initialAngle, scaleFactor):
        self.window = NLDGraphWin("Fractal Tree", 600, 600, [-5,-.1,5,9.1])
        self.initialAngle = math.radians(initialAngle)
        self.scaleFactor = scaleFactor

    def drawLine(self, startPoint, length, direction, color='black', width=3):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        l = Line(ogPoint, startPoint)
        l.setFill(color)
        l.setWidth(width)
        l.draw(self.window)

    def drawTreeRec(self, level, point, length, angle, animated=True, colored=True, randomLength=False, leftFactor=1, rightFactor=1, widthScaling=True, width=10):
        if width < 1:
            width = 1

        if level < 2:
            self.drawLine(point, length, angle, 'darkgreen',width)
        else:
            self.drawLine(point, length, angle, 'saddlebrown',width)

        #if animated:
        #    self.window.update()

        if level != -1:
            #Could change where branches off from AND how many branches come from another branch (for loop system for recursive calls)
            point2 = copy.copy(point)
            self.drawTreeRec(level-1, point, length * self.scaleFactor, angle - rightFactor*self.initialAngle, width=(width-1 if widthScaling else width))
            self.drawTreeRec(level-1, point2, length * self.scaleFactor, angle + leftFactor*self.initialAngle, width=(width-1 if widthScaling else width))

def main():
    tree = FractalTree(-30, .75)

    tree.drawTreeRec(20, Point(0,0), 1, math.radians(90), animated=False)

    tree.window.getMouse()
    tree.window.close()

if __name__ == '__main__':
    main()
