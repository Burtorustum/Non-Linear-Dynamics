#MandelbrotSet.py
from graphics import *
from nld_graphics import *
import numpy as np
import time as time
import matplotlib.pyplot as plt

class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = NLDGraphWin("Complex Plane", pixelWidth, pixelHeight, [-2.1,-1.4,.8,1.4])

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

    def regPlotSet(self, maxIterates=10000):
        start = time.time()
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

        for i in range(len(c)):
            for ii in range(len(c[i])):
                #if not diverge[i][ii]:
                    #z = c[i][ii]
                    #self.window.plot(z.real,z.imag)
                it = divergeIter[i][ii]
                if it != maxIterates:
                    z = c[i][ii]
                    color = 255 - it * 10
                    if color < 5:
                        color = 5
                    self.window.plot(z.real, z.imag, color_rgb(color, color, color))
        self.window.update()
        print("runtime:", time.time()-start)


m = MandelbrotSet(800, 800)
#numoutput = m.numPlotSet()
#plt.imshow(numoutput)
regoutput = m.regPlotSet()
m.window.getMouse()
m.window.close()
