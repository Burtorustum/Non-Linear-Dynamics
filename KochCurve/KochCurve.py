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
        self.initalPoint = None
        self.curAngle = 0
        self.height = 1/(2*math.sin(self.initialAngle)+2)

    def drawLine(self, startPoint, length, direction):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(direction)
        deltaY = length * math.sin(direction)
        startPoint.move(deltaX, deltaY)
        Line(ogPoint, startPoint).draw(self.window)

    def drawCurveRec(self, startPoint, length, level, viewMode, colored):
        if colored:
            Polygon(startPoint, ).draw(self.window)
        if(level == 0):
            self.drawLine(startPoint, length, self.curAngle)
            if (viewMode == 'animated'):
                self.window.update()
        else:
            length *= self.height
            self.drawCurveRec(startPoint, length, level - 1, viewMode, colored)
            self.curAngle += self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode, colored)
            self.curAngle -= 2 * self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode, colored)
            self.curAngle += self.initialAngle
            self.drawCurveRec(startPoint, length, level - 1, viewMode, colored)

        if(viewMode == 'animated'):
            self.window.setCoords(startPoint.getX()-.05*self.initialLength/(2*self.level), startPoint.getY()-.05*self.initialLength/(2*self.level), startPoint.getX()+.05*self.initialLength/(2*self.level), startPoint.getY()+.05*self.initialLength/(2*self.level))
        elif(viewMode == 'cinema'):
            if startPoint.getX() > self.maxX.getX():
                self.maxX = startPoint
            self.scaleWindow(self.maxX)

    def drawCurve(self, startPoint, level, overallDirection, viewMode, colored):
        self.level = copy.copy(level)
        self.initalPoint = copy.copy(startPoint)
        self.startPoint = copy.copy(startPoint)
        self.curAngle = math.radians(overallDirection)
        self.maxX = copy.copy(startPoint)
        self.drawCurveRec(startPoint, self.initialLength, level, viewMode, colored)
        self.endPoint = copy.copy(startPoint)
        if viewMode== 'animated':
            self.animatedScaleWindow(self.endPoint)
        elif viewMode == 'regular':
            self.scaleWindow(self.endPoint)
        elif viewMode == 'cinema':
            self.scaleWindow(self.maxX)

    def drawPolygon(self, startPoint, level, numSides, inner=False):
        maxX = 0
        maxY = 0
        minX = 0
        minY = 0
        for side in range(numSides):
            self.drawCurve(startPoint, level, (1 if inner else -1)*(360/numSides)*side, 'None', False)
            if startPoint.getX() > maxX:
                maxX = startPoint.getX()
            if startPoint.getY() > maxY:
                maxY = startPoint.getY()
            if startPoint.getX() < minX:
                minX = startPoint.getX()
            if startPoint.getY() < minY:
                minY = startPoint.getY()

        if not inner:
            self.window.setCoords(minX-.01, minY-.01, maxX+.01, maxY+.01)
        else:
            self.window.setCoords(minX - self.height - .01, minY - self.height - .01, maxX + self.height + .01, maxY + self.height + .01)
        self.window.update()

    def scaleWindow(self, pointCurrent):
        maxY = self.height
        minY = 0
        maxX = pointCurrent.getX()
        minX = 0
        while abs(maxX - minX) < abs(maxY - minY):
            maxX += .01
            minX -= .01
        while abs(maxX - minX) > abs(maxY - minY):
            maxY += .001
            minY -= .001
        self.window.setCoords(minX, minY, maxX, maxY)
        self.window.update()

    def animatedScaleWindow(self, pointCurrent):
        maxY = self.height
        minY = 0
        maxX = pointCurrent.getX()+.001
        minX = 0

        while abs(maxX - minX) < abs(maxY - minY):
            maxX += .01
            minX -= .01
        while abs(maxX - minX) > abs(maxY - minY):
            maxY += .001
            minY -= .001

        curMaxY = copy.copy(pointCurrent.getY())
        curMinY = copy.copy(pointCurrent.getY())
        curMaxX = copy.copy(pointCurrent.getX())
        curMinX = copy.copy(pointCurrent.getX())

        while abs(curMaxX - curMinX) < abs(maxX - minX):
            while abs(curMaxX - curMinX) < abs(curMaxY - curMinY):
                curMaxX += .01
                curMinX -= .01
            while abs(curMaxX - curMinX) > abs(curMaxY - curMinY):
                curMaxY += .001
                curMinY -= .001
            curMaxX = maxX
            curMinX -= .001
            curMaxY += .001
            self.window.setCoords(curMinX, curMinY, curMaxX, curMaxY)
            self.window.update()

def main():
    angle = 60
    length = 1
    curve = KochCurve(angle, length)
    point = Point(0,0)
    curve.drawPolygon(point, 6, 3)
    #curve.drawCurve(point, 5, 0, "animated", True)
    curve.window.getMouse()
    curve.window.close()

if __name__ == '__main__':
    main()
