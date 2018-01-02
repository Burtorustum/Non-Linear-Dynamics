#MandelbrotSet.py
from nld_graphics import *
import numpy as np
import time as time
import matplotlib.pyplot as plt

class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = NLDGraphWin("Complex Plane", pixelWidth, pixelHeight, [-2.1,-1.4,.8,1.4])
        self.zoomcount = 0

    def numPlotSet(self, maxIterates=100):
        y, x = np.ogrid[-1.4:1.4:self.window.height*1j, -2.1:0.8:self.window.width*1j]
        c = x + y*1j
        z = c
        divergeIter = maxIterates + np.zeros(z.shape, dtype=int)

        for i in range(maxIterates):
            z = z**2 + c
            diverge = abs(z) > 2
            divergingNow = diverge & (divergeIter == maxIterates)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        return divergeIter

    def regPlotSet(self, maxIterates=5000, fill = False):
        start = time.time()
        y, x = np.ogrid[self.window.currentCoords[1]:self.window.currentCoords[3]:self.window.height*1j, self.window.currentCoords[0]:self.window.currentCoords[2]:self.window.width*1j]
        c = x + y*1j
        z = c
        divergeIter = maxIterates + np.zeros(z.shape, dtype=int)

        for i in range(maxIterates):
            z = z**2 + c
            diverge = abs(z) >= 2
            divergingNow = diverge & (divergeIter == maxIterates)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                it = divergeIter[i][ii]
                if it != maxIterates:
                    z = c[i][ii]
                    color = 255 - it * abs(10 - 2 * self.zoomcount)
                    if color < 5 & fill:
                        color = 5
                    elif color < 5:
                        color = 0
                    self.window.plot(z.real, z.imag, color_rgb(color, color, color))
                elif fill:
                    z = c[i][ii]
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


m = MandelbrotSet(800, 800)

#Using matplotlib:
#numoutput = m.numPlotSet()
#plt.imshow(numoutput)

#Using graphics.py:
m.regPlotSet(fill = True)
m.zoom(True)
m.zoom(True)
m.window.getMouse()
m.zoom(inout="out", fill=True)
m.window.getMouse()
m.window.close()
