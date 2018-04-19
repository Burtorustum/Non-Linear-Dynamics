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

    def drawLine(self, startPoint, length, direction):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        Line(ogPoint, startPoint).draw(self.window)

    def drawCurveRec(self, startPoint, length, level, viewMode):
        if(level == 0):
            self.drawLine(startPoint, length, self.curAngle)
            if (viewMode == 'animated'):
                self.window.update()
        else:
            length *= self.height
            #TODO: Fix the length adjustment so that it makes 4 even segments correctly.
            self.drawCurveRec(startPoint, length, level - 1, viewMode)
            self.curAngle += self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode)
            self.curAngle -= 2 * self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode)
            self.curAngle += self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode)

        if(viewMode == 'animated'):
            self.window.setCoords(startPoint.getX()-.05*self.initialLength, startPoint.getY()-.05*self.initialLength, startPoint.getX()+.05*self.initialLength, startPoint.getY()+.05*self.initialLength)
        elif(viewMode == 'cinema'):
            self.scaleWindow(startPoint)

    def drawCurve(self, startPoint, level, overallDirection, viewMode):
        self.startPoint = copy.copy(startPoint)
        self.curAngle = math.radians(overallDirection)
        self.drawCurveRec(startPoint, self.initialLength, level, viewMode)
        self.endPoint = copy.copy(startPoint)
        if viewMode== 'animated':
            self.animatedScaleWindow(self.endPoint)
        elif viewMode == 'regular' or viewMode ==
        self.scaleWindow(self.endPoint)

    def drawPolygon(self, startPoint, level, numSides):
        maxX = 0
        maxY = 0
        minX = 0
        minY = 0
        for side in range(numSides):
            self.drawCurve(startPoint, level, (360/numSides)*side, 'regular')
            if startPoint.getX() > maxX:
                maxX = startPoint.getX()
            if startPoint.getY() > maxY:
                maxY = startPoint.getY()
            if startPoint.getX() < minX:
                minX = startPoint.getX()
            if startPoint.getY() < minY:
                minY = startPoint.getY()

        self.window.setCoords(minX, minY, maxX, maxY)
        self.window.update()

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

    def animatedScaleWindow(self, pointCurrent):
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

        curMaxY = copy.copy(pointCurrent.getY())
        curMinY = copy.copy(pointCurrent.getY())
        curMaxX = copy.copy(pointCurrent.getX())
        curMinX = copy.copy(pointCurrent.getX())

        while abs(curMaxX - curMinX) < abs(maxX - minX):
            while abs(curMaxX - curMinX) < abs(curMaxY - curMinY):
                curMaxX += .01
                curMinX -= .01
            while abs(curMaxX - curMinX) > abs(curMaxY - curMinY):
                curMaxY += .005
                curMinY -= .005
            curMaxX = maxX
            curMinX -= .005
            curMaxY += .005
            self.window.setCoords(curMinX, curMinY, curMaxX, curMaxY)
            self.window.update()
        self.scaleWindow(pointCurrent)

def main():
    angle = 60
    length = 1
    curve = KochCurve(angle, length)
    point = Point(0,0)
    curve.drawPolygon(point, 6, 7)
    #curve.drawCurve(point, 3, 0, "animated")
    curve.window.getMouse()
    curve.window.close()

if __name__ == '__main__':
    main()
