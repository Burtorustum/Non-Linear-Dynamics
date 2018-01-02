#JuliaSet.py

from nld_graphics import *
import numpy as np
import time as time

class JuliaSet:
    def __init__ (self, pixelWidth, pixelHeight):
        self.window = NLDGraphWin("Complex Plane", pixelWidth, pixelHeight, [-2,-2,2,2])
        self.zoomcount = 0

    def regPlotSet(self, maxIterates=1000, const = .365 - 0.37j, fill = False):
        start = time.time()
        y, x = np.ogrid[self.window.currentCoords[1]:self.window.currentCoords[3]:self.window.height*1j, self.window.currentCoords[0]:self.window.currentCoords[2]:self.window.width*1j]
        c = x + y*1j
        z = c
        divergeIter = maxIterates + np.zeros(z.shape, dtype=int)

        for i in range(maxIterates):
            z = z**2 + const
            diverge = abs(z) >= 5000
            divergingNow = diverge & (divergeIter == maxIterates)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                z = c[i][ii]
                it = divergeIter[i][ii]
                if it != maxIterates:
                    #TODO: Need to add layering to the colors... not only grayscale but over some iterate start redscale or something
                    color = 255 - it * abs(8 - 2 * self.zoomcount)
                    if color < 5 & fill:
                        color = 5
                    elif color < 5:
                        color = 0
                    self.window.plot(z.real, z.imag, color_rgb(color, color, color))
                elif fill:
                    self.window.plot(z.real, z.imag, color_rgb(100, 0, 0))
        self.window.update()
        print("runtime:", time.time()-start)

    def zoom(self, inout="in", fill=False):
        if inout == "in":
            self.zoomcount += 1
        else:
            self.zoomcount = 0
        self.window.zoom(inout)
        self.regPlotSet(fill=fill)

m = JuliaSet(800, 800)
m.regPlotSet(fill = False, const= -0.123 + 0.745j)
#0
#1j
#-1j
#-0.123 + 0.745j
#-0.77 + 0.22j
#.365 - 0.37j
m.window.getMouse()
m.window.close()
