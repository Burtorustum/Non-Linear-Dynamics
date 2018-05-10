#FractalTree.py
import copy as copy
import math as math
from nld_graphics import *
from graphics import *
class FractalTree:

    def __init__(self, initialAngle, scaleFactor):
        self.window = NLDGraphWin("Fractal Tree", 600, 600, [-5,-.1,5,4.1])
        self.initialAngle = math.radians(initialAngle)
        self.scaleFactor = scaleFactor

    def drawLine(self, startPoint, length, direction):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        Line(ogPoint, startPoint).draw(self.window)

    def drawTreeRec(self, level, point, length, angle, animated=True):
        if level != -1:
            self.drawLine(point, length, angle)
            point2 = copy.copy(point)
            self.drawTreeRec(level-1, point, length * self.scaleFactor, angle - self.initialAngle)
            self.drawTreeRec(level-1, point2, length * self.scaleFactor, angle + self.initialAngle)
            if animated:
                self.window.update()

def main():
    tree = FractalTree(30, .75)
    tree.drawTreeRec(9, Point(0,0), 1, math.radians(90))
    tree.window.getMouse()
    tree.window.close()

if __name__ == '__main__':
    main()
