#MandelbrotSet.py
from graphics import *
from nld_graphics import *
import numpy as np
import time as time
import matplotlib.pyplot as plt
import matplotlib.colors as color

class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = NLDGraphWin("Complex Plane", pixelWidth, pixelHeight, [-2,-2,2,2])

    def numPlotSet(self, maxIterates=100):
        self.yPoints = np.linspace(-1.4, 1.4, self.window.height)
        self.xPoints = np.linspace(-2.1, 0.8, self.window.width)

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
        None

m = MandelbrotSet(800, 800)
numoutput = m.plotSet()
regoutput = m.regPlotSet()
print(m.yPoints)
print(m.xPoints)
