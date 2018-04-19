#KochCurve.py
from nld_graphics import *
from graphics import *
import math as math
import copy as copy

class KochCurve:

    def __init__ (self, initialAngle, initialLength):
        self.window = NLDGraphWin("Koch Curve", 600, 600, [-1,-1,1,1])
        self.initialAngle = math.radians(initialAngle)
        self.initialLength = initialLength
        self.startPoint = None
        self.curAngle = 0
        self.height = 1/(2*math.sin(self.initialAngle)+2)

    def drawLine(self, startPoint, length, direction, viewMode):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        Line(ogPoint, startPoint).draw(self.window)
        if (viewMode == 'animated'):
            self.window.update()

    def drawCurveRec(self, startPoint, length, level, viewMode):
        if(level == 0):
            self.drawLine(startPoint, length, self.curAngle, viewMode)
        else:
            length /= math.co
            self.drawCurveRec(startPoint, length, level - 1, viewMode)
            self.curAngle += self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode)
            self.curAngle -= 2 * self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode)
            self.curAngle += self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode)

        if(viewMode == 'animated'):
            self.window.setCoords(startPoint.getX()-.05, startPoint.getY()-.05, startPoint.getX()+.05, startPoint.getY()+.05)
        elif(viewMode == 'cinema'):
            self.scaleWindow(startPoint)

    def drawCurve(self, startPoint, level, viewMode):
        self.startPoint = copy.copy(startPoint)
        self.drawCurveRec(startPoint, self.initialLength, level, viewMode)
        self.endPoint = copy.copy(startPoint)
        self.scaleWindow(self.endPoint)

    def scaleWindow(self, pointCurrent):
        maxY = self.height if self.initialAngle >= 0 else 0
        minY = 0 if self.initialAngle >= 0 else self.height * -1
        maxX = pointCurrent.getX()
        minX = 0
        while abs(maxX - minX) < abs(maxY - minY):
            maxX += .01
            minX -= .01
        while abs(maxX - minX) > abs(maxY - minY):
            maxY += .005
            minY -= .005
        self.window.setCoords(minX-.01, minY, maxX+.01, maxY)
        self.window.update()

def main():
    angle = 60
    length = 1
    curve = KochCurve(angle, length)
    curve.drawCurve(Point(0,0), 5, 'animated')
    curve.window.getMouse()
    curve.window.close()

if __name__ == '__main__':
    main()
