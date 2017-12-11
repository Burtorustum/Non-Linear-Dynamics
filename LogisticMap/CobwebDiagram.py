#TimeSeries.py
from graphics import *
from random import random

class CobwebDiagram:
    function = None
    window = None
    coords = None
    flushing = None
    coords = [-.1,-.1,1.1,1.1]
    r = 3.5
    x0 = random()

    #initialize the cobweb object
    def __init__ (self, function=True, flush = True, win=GraphWin("Cobweb Diagram", 600, 600, False)):
        self.function = function
        if function == True:
            def logisticMap(x,r):
                return r * x * (1.0 - x)
            self.function = logisticMap

        self.window = win
        self.flushing = flush

        self.window.setCoords(self.coords[0],self.coords[1],self.coords[2],self.coords[3])

        ax1 = Line(Point(0, 0), Point(1, 0))
        ax1Label = Text(Point(.5,-.05),"Xn")

        ax2 = Line(Point(0, 0), Point(0, 1))
        ax2Label = Text(Point(-.05, .5), "Xn+1")

        steadystate = Line(Point(0, 0), Point(1, 1))

        ax1.draw(self.window)
        ax1Label.draw(self.window)
        ax2.draw(self.window)
        ax2Label.draw(self.window)
        steadystate.draw(self.window)

        self.drawCobwebDiagram()

    def drawCobwebDiagram(self, x0=random(), iterates = 50):
        self.window.clear()
        r = self.r
        x = 0
        while x <= 1:
            self.window.plot(x, self.function(x,r), 'black')
            x += .0005
        self.window.update()

        lastX = x0
        lastY = 0
        movingX = False
        for i in range(iterates):
            if movingX==True:
                movingX = False
                width = lastY
                if lastX < width:
                    while lastX < width:
                        self.window.plot(lastX, lastY, 'red')
                        lastX+=.001
                else:
                    while lastX > width:
                        self.window.plot(lastX, lastY, 'red')
                        lastX-=.001

            else:
                movingX = True
                height = self.function(lastX,r)
                if lastY < height:
                    while lastY < height:
                        self.window.plot(lastX, lastY, 'red')
                        lastY+=.001
                else:
                    while lastY > height:
                        self.window.plot(lastX, lastY, 'red')
                        lastY-=.001
        self.window.update()

    def setR(self, r):
        self.r = r
        self.drawCobwebDiagram(x0 = self.x0)
    def setx0(self, x0):
        self.x0 = x0
        self.drawCobwebDiagram(x0 = self.x0)

def main():
    g = CobwebDiagram()
    g.drawCobwebDiagram(2,.5)
    g.window.getMouse()
    g.drawCobwebDiagram(3,.25)
    g.window.getMouse()
    g.window.close()

if __name__ == "__main__":
    main()
