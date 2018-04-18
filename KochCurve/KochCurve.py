#KochCurve.py
from nld_graphics import *
from graphics import *
import math as math
import copy as copy

class KochCurve:

    def __init__ (self, initialAngle):
        self.window = NLDGraphWin("Koch Curve", 600, 600, [-1,-1,1,1])
        self.initialAngle = initialAngle
        self.startPoint = None
        self.curAngle = 0

    def drawLine(self, startPoint, length, direction, cinemaView):
        ogPoint = copy.copy(startPoint)
        deltaX = length * math.cos(math.radians(direction))
        deltaY = length * math.sin(math.radians(direction))
        startPoint.move(deltaX, deltaY)
        Line(ogPoint, startPoint).draw(self.window)
        if (cinemaView):
            self.window.update()

    def drawCurveRec(self, startPoint, length, level, cinemaView):
        if(level == 0):
            self.drawLine(startPoint, length, self.curAngle, cinemaView)
        else:
            length /= 3.0
            self.drawCurve(startPoint, length, level - 1, cinemaView)
            self.curAngle += self.initialAngle
            self.drawCurve(startPoint, length, level - 1, cinemaView)
            self.curAngle -= 2 * self.initialAngle
            self.drawCurve(startPoint, length, level - 1, cinemaView)
            self.curAngle += self.initialAngle
            self.drawCurve(startPoint, length, level - 1, cinemaView)

    def drawCurve(self, startPoint, length, level, cinemaView):
        self.startPoint = copy.copy(startPoint)
        self.drawCurveRec(startPoint, length, level, cinemaView)
        self.endPoint = copy.copy(startPoint)
        if(cinemaView):
            self.window.setCoords(self.startPoint.getX()-.05, self.startPoint.getY()-.05, startPoint.getX()+.05, startPoint.getY()+.05)

def main():
    pointeroo = Point(0,0)
    angle = 60
    curve = KochCurve(angle)
    curve.drawCurve(pointeroo, 1, 5, True)
    maxY = 1/(2*math.sin(math.radians(angle))+2)
    minY = 0
    maxX = 1
    minX = 0
    while abs(maxX - minX) < abs(maxY - minY):
        maxX += .01
        minX -= .01
    while abs(maxX - minX) > abs(maxY - minY):
        maxY += .005
        minY -= .005
    curve.window.setCoords(minX-.01, minY, maxX+.01, maxY)
    curve.window.update()
    curve.window.getMouse()
    curve.window.close()

if __name__ == '__main__':
    main()
