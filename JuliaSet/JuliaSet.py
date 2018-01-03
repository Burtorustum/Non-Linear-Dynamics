#JuliaSet.py

from nld_graphics import *
import numpy as np
import time as time
from random import random

class JuliaSet:
    def __init__ (self, pixelWidth, pixelHeight):
        self.hqwindow = NLDGraphWin("HQ Julia Set", pixelWidth, pixelHeight, [-2,-2,2,2])
        self.lqwindow = NLDGraphWin("LQ Julia Set", pixelWidth, pixelHeight, [-2,-2,2,2])

    def regPlotSet(self, maxIterates = 750, const = .365 - 0.37j, fill = False):
        start = time.time()
        y, x = np.ogrid[self.hqwindow.currentCoords[1]:self.hqwindow.currentCoords[3]:self.hqwindow.height*1j, self.hqwindow.currentCoords[0]:self.hqwindow.currentCoords[2]:self.hqwindow.width*1j]
        c = x + y*1j
        z = c
        divergeIter = maxIterates + np.zeros(z.shape, dtype=int)

        for i in range(maxIterates):
            z = z**2 + const
            diverge = abs(z) >= 2
            divergingNow = diverge & (divergeIter == maxIterates)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                it = divergeIter[i][ii]
                if it != maxIterates:
                    #TODO: Need to add layering to the colors... not only grayscale but over some iterate start redscale or something
                    z = c[i][ii]
                    color = 255 - it * 5
                    if color < 5 & fill:
                        color = 5
                    elif color < 5:
                        color = 0
                    self.hqwindow.plot(z.real, z.imag, color_rgb(color, color, color))
                elif fill:
                    z = c[i][ii]
                    self.hqwindow.plot(z.real, z.imag, color_rgb(100, 0, 0))
        self.hqwindow.update()
        print("hq runtime:", time.time()-start)

    def inversePlotSet(self, maxIterates = 750, const = .365 - 0.37j):
        def g(z, c = const):
            i = 1
            if random() < .5:
                i = -1
            return i * (z-c) ** 0.5
        start = time.time()
        z = complex(-1000 + 2000 *random(), -1000 + 2000*random())

        for i in range (10000):
            z = g(z)

        for i in range(5000):
            z = g(z)
            self.lqwindow.plot(z.real, z.imag, 'black')

        self.lqwindow.update()
        print ("lq runtime: ", time.time()-start)

    def zoom(self, inout="in", fill=False):
        self.hqwindow.zoom(inout)
        self.regPlotSet(fill=fill)

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
