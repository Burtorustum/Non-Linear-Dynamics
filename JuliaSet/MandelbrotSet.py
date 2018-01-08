#MandelbrotSet.py
from nld_graphics import *
import numpy as np
import time as time
import matplotlib.pyplot as plt

class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = NLDGraphWin("Mandelbrot Set", pixelWidth, pixelHeight, [-2.1,-1.4,.8,1.4])
        self.window.setBackground('black')
        self.zoomcount = 0
        self.oldScheme = False

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

    def regPlotSet(self, maxIterates=50):
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
                    if it <= 40:
                        color = it * 6 + 50
                        if color > 255:
                            color = 255
                        self.window.plot(z.real, z.imag, color_rgb(0, 0, color))
                    else:
                        color = 255 - it * 3
                        if color < 0:
                            color = 1
                            self.window.plot(z.real, z.imag, color_rgb(color, color * 10, 0))
        self.window.update()
        #print("Mandelbrot Runtime:", time.time()-start)

    #TODO: Force coordinates to hold ratio.
    def zoom(self, inout="in", iterates=250):
        self.window.zoom(inout)
        self.regPlotSet(maxIterates=iterates)


if __name__ == "__main__":
    m = MandelbrotSet(800, 800)

    #Using matplotlib:
    #numoutput = m.numPlotSet()
    #plt.imshow(numoutput)

    #Using graphics.py:
    m.regPlotSet(maxIterates=50)
    m.zoom(iterates=1000)
    m.zoom(iterates=5000)

    m.window.getMouse()
    m.window.close()
