#Bifurcation Diagram class
from graphics import *
from math import *
from random import random

class BifurcationDiagram:
    function = None
    window = None
    coords = None
    originalCoords = [0,0,0,0]
    flushing = None

    def __init__ (self, function=True, flush=True, window=GraphWin("Bifurcation Diagram", 1200, 500, False), coords = [0.75,0,4,1]):
        self.function = function
        if function == True:
            def logisticMap(x,r):
                return r * x * (1.0 - x)
            self.function = logisticMap

        self.window = window
        self.coords = coords
        self.flushing = flush

        #So that the memory locations are not linked
        for p in range(4):
            self.originalCoords[p] = coords[p]

        self.window.setCoords(self.coords[0],self.coords[1],self.coords[2],self.coords[3])
        self.drawBifurcationDiagram()

    def drawBifurcationDiagram(self, numTransients = 10000, numIterates = 500):
        self.window.clear()
        count = 0
        r = self.coords[0]
        rstep = (self.coords[2] - self.coords[0])/self.window.width

        while r < self.coords[2]:
            x0 = random()

            for n in range(numTransients):
                x0 = self.function(x0,r)

            for n in range(numIterates):
                x0 = self.function(x0,r)
                self.window.plot(r, x0, 'red')
            r += rstep
            count += 1
            if self.flushing and count % 10 == 0:
                self.window.update()
        self.window.update()

    def zoom(self):
        x0 = random()
        r = self.coords[2]

        for n in range(10000):
            x0 = self.function(x0,r)

        max = self.function(x0,r)
        min = self.function(x0,r)

        for n in range(300):
            x0 = self.function(x0,r)
            if x0 < min:
                min = x0
            if x0 > max:
                max = x0

        self.coords[1] = min - .025
        self.coords[3] = max + .025

        self.window.setCoords(self.coords[0],self.coords[1],self.coords[2],self.coords[3])
        self.drawBifurcationDiagram()

    def oneClickZoom(self):
        point = self.window.getMouse()

        self.coords[0] = point.getX() - .25 * (point.getX() - self.coords[0])
        self.coords[2] = point.getX() + .25 * (self.coords[2] - point.getX())
        if self.coords[0] < self.originalCoords[0]:
            self.coords[0] = self.originalCoords[0]
        if self.coords[2] > self.originalCoords[2]:
            self.coords[2] = self.originalCoords[2]

        self.zoom()

    def twoClickZoom(self):
        point1 = self.window.getMouse()
        point2 = self.window.getMouse()

        if point1.getX() < point2.getX():
            self.coords[0] = point1.getX()
            self.coords[2] = point2.getX()
        else:
            self.coords[2] = point1.getX()
            self.coords[0] = point2.getX()

        if self.coords[0] < self.originalCoords[0]:
            self.coords[0] = self.originalCoords[0]
        if self.coords[2] > self.originalCoords[2]:
            self.coords[2] = self.originalCoords[2]

        self.zoom()

    def zoomout(self):
        self.coords[0] = self.originalCoords[0]
        self.coords[1] = self.originalCoords[1]
        self.coords[2] = self.originalCoords[2]
        self.coords[3] = self.originalCoords[3]
        self.window.setCoords(self.coords[0],self.coords[1],self.coords[2],self.coords[3])
        self.drawBifurcationDiagram()


def main():
    def tentMap(x, r):
        if x < .5:
            return x*r
        return r*(1-x)

    #g = BifurcationDiagram(function=tentMap, coords = [1,0,2,1])
    g = BifurcationDiagram(flush=True)
    while True:
        g.twoClickZoom()
    g.window.getMouse()
    g.window.close()

if __name__ == "__main__":
    main()
