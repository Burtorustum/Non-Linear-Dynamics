#MandelbrotSet.py
from graphics import *
from nld_graphics import *
import numpy as np
import time as time
import matplotlib.pyplot as plt

class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = NLDGraphWin("Complex Plane", pixelWidth, pixelHeight, [-1.4,-2.1,1.4,0.8])

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

    def regPlotSet(self, maxIterates=100):
        y, x = np.ogrid[-1.4:1.4:self.window.height*1j, -2.1:0.8:self.window.width*1j]
        c = x + y*1j
        z = c

        for i in range(maxIterates):
            z = z**2 + c
            diverge = abs(z) > 2
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                if diverge[i][ii]:
                    z = c[i][ii]
                    self.window.plot(z.real,z.imag)
        self.window.update()


m = MandelbrotSet(800, 800)
regoutput = m.regPlotSet()
m.window.getMouse()
m.window.close()
