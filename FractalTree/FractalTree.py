#FractalTree.py
import copy as copy
import math as math
from nld_graphics import *

class FractalTree:

    def __init__(self, initialAngle, scaleFactor):
        self.window = NLDGraphWin("Fractal Tree", 600, 600, [-5,-.1,5,9.1])
        self.initialAngle = math.radians(initialAngle)
        self.scaleFactor = scaleFactor

    def drawLine(self, startPoint, length, direction, color='black'):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        l = Line(ogPoint, startPoint)
        l.setFill(color)
        l.setWidth(3)
        l.draw(self.window)

    def drawTreeRec(self, level, point, length, angle, animated=False, colored=True, randomLength=False, leftFactor=1, rightFactor=1):
        if level < 2:
            self.drawLine(point, length, angle, 'darkgreen')
        else:
            self.drawLine(point, length, angle, 'saddlebrown')
        if level != -1:
            #Could change where branches off from AND how many branches come from another branch (for loop system for recursive calls)
            point2 = copy.copy(point)
            self.drawTreeRec(level-1, point, length * self.scaleFactor, angle - rightFactor*self.initialAngle)
            self.drawTreeRec(level-1, point2, length * self.scaleFactor, angle + leftFactor*self.initialAngle)
            if animated:
                self.window.update()

def main():
    tree = FractalTree(30, .75)

    tree.drawTreeRec(9, Point(0,0), 1, math.radians(90), rightFactor=.25)

    tree.window.getMouse()
    tree.window.close()

if __name__ == '__main__':
    main()
