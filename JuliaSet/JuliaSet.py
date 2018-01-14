#JuliaSet.py

from nld_graphics import *
import numpy as np
import time as time
from random import random

class JuliaSet:
    def __init__ (self, pixelWidth, pixelHeight):
        self.lqwindow = NLDGraphWin("LQ Julia Set", pixelWidth, pixelHeight, [-2,-2,2,2])
        self.hqwindow = NLDGraphWin("HQ Julia Set", pixelWidth, pixelHeight, [-2,-2,2,2])
        self.hqwindow.setBackground(color_rgb(75,75,255))
        self. maxIterates = 2000

    def regPlotSet(self, const = .365 - 0.37j):
        start = time.time()
        y, x = np.ogrid[self.hqwindow.currentCoords[1]:self.hqwindow.currentCoords[3]:self.hqwindow.height*1j, self.hqwindow.currentCoords[0]:self.hqwindow.currentCoords[2]:self.hqwindow.width*1j]
        c = x + y*1j
        z = c
        divergeIter = self.maxIterates + np.zeros(z.shape, dtype=int)

        for i in range(self.maxIterates):
            z = z**2 + const
            diverge = abs(z) >= 2
            divergingNow = diverge & (divergeIter == self.maxIterates)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                it = divergeIter[i][ii]
                if it != self.maxIterates:
                    z = c[i][ii]
                    if it <= 40:
                        color = it * 6 + 50
                        if color > 255:
                            color = 255
                        self.hqwindow.plot(z.real, z.imag, color_rgb(0, 0, color))
                    else:
                        color = 255 - it * 3
                        if color < 0:
                            color = 1
                            self.hqwindow.plot(z.real, z.imag, color_rgb(color, color * 10, 0))
        self.hqwindow.update()
        print("HQ Runtime:", time.time()-start, "for a c value of:", const)

    def inversePlotSet(self, const = .365 - 0.37j):
        def g(z, c = const):
            i = 1
            if random() < .5:
                i = -1
            return i * (z-c) ** 0.5
        start = time.time()
        z = complex(-3+ 3 *random(), -3+ 3*random())

        for i in range (10000):
            z = g(z)

        for i in range(5000):
            z = g(z)
            self.lqwindow.plot(z.real, z.imag, 'black')

        self.lqwindow.update()
        #print ("LQ Runtime:", time.time()-start, "for a c value of:", const)

    def zoom(self, inout="in", iterates=250, fill=False, constan = .365 - 0.37j):
        self.hqwindow.zoom(inout)
        self.regPlotSet(fill=fill, const = constan)

if __name__ == '__main__':
    m = JuliaSet(800, 800)
    #m.regPlotSet(const = 0.35)
    #m.hqwindow.getMouse()
    #m.hqwindow.close()

    m.inversePlotSet()
    m.lqwindow.getMouse()
    m.lqwindow.close()

#0
#1j
#-1j
#-0.123 + 0.745j
#-0.77 + 0.22j
#.365 - 0.37j
#-0.8+0.156j
#-0.835-0.2321j
#-0.4+0.6j
#0.279
