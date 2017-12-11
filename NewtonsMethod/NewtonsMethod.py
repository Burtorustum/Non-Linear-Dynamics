from graphics import *
from nld_graphics import *
from math import *
import cmath as cmath
import time as time
from sympy import *
import numpy as np

class NewtonsMethod:
    def __init__ (self, func, sym, pixelWidth=600, pixelHeight=600, coords=[-3,-3,3,3], colors=('red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown','black')):
        self.window = NLDGraphWin("Complex Plane", pixelWidth, pixelHeight, coords)
        self.symbol = symbol
        self.updateFunc(function=func, symbol=sym)
        self.colors = colors
        self.flushing = False
        self.shading = False
        self.reltol = 1e-6
        self.quality=1
        self.altcolors=("#D2ACD3","#8B76A1","#C587AE","#F5B9C9","#FBCDBE","#FDEEC7","#5DBCD2")
        self.useAlts = False
        self.iterations = 34

        #print(self.symbol)
        #print(self.__func)
        #print(self.__funcPrime)
        #print('roots' + str(self.roots))

    def plotZ(self, z, color = 'black'):
        try:
            self.window.plot(z.real, z.imag, color)
        except:
            self.window.plot(z[0], z[1], color)

    def newton(self, z):
        return z - complex(self.useFunc(z)/self.useFuncPrime(z))

    def useFunc(self, z):
        return self.__func(z)

    def useFuncPrime(self, z):
        return self.__funcPrime(z)

    def updateFunc(self, function, symbol):
        self.symbol = symbol
        self.__func = function
        self.updateDerivative()
        self.updateRoots()
        self.__func = lambdify(self.symbol, function)

    def updateDerivative(self):
        self.__funcPrime = lambdify(self.symbol, diff(self.__func, self.symbol))

    def updateRoots(self):
        temp = roots(self.__func, multiple=True)
        for i in range(len(temp)):
            temp[i] = complex(temp[i])

        self.roots = temp

    def optimizeIterates(self):
        startTime = time.time()
        iterAll = []
        looking = True
        reals = self.window.currentCoords[0]
        imags = self.window.currentCoords[1]
        realNumerator = (self.window.currentCoords[2] - reals) * self.quality
        imagNumerator = (self.window.currentCoords[3] - imags) * self.quality
        imagStep = imagNumerator/self.window.height
        realStep = realNumerator/self.window.width
        for i in range(0, 90000):
            z = complex(reals + realStep * i, imags + imagStep * i)
            looking = True
            newIterate = -1
            while looking:
                newIterate += 1
                if newIterate >= 1000:
                    looking = False
                try:
                    z = self.newton(z)
                    #print(z)
                except:
                    looking = False
                for x in range(0,len(self.roots)):
                    if cmath.isclose(z, self.roots[x], rel_tol = self.reltol):
                        looking = False
                        iterAll.append(newIterate)
            #print(z)
            if time.time() - startTime > 180:
                print("Failed to find optimal iterations. Note the function as this should never happen unless roots are unknown for a function.")
                return self.iterations
        return max(iterAll)

    #needs work
    def getColor(self, colorNum, iterates):
        color = self.colors[colorNum]
        if iterates > 255:
            iterates = 255
        if color == 'red':
            return color_rgb(255-iterates, 0, 0)
        if color == 'green':
            return color_rgb(0, 255-iterates, 0)
        if color == 'blue':
            return color_rgb(0, 0, 255-iterates)
        if color == 'black':
            return color_rgb(iterates,iterates, iterates)
        if color == 'yellow':
            return color_rgb(255-iterates, 255-iterates, 0)
        if color == 'orange':
            return color_rgb(255, 165 - iterates/2, 0)
        if color == 'purple':
            return color_rgb(128-iterates/2, 128-iterates/2, 0)
        if color == 'pink':
            return color_rgb(255-iterates/2, 192-iterates/2, 203-iterates/2)

    def draw(self):
        startTime = time.time()
        reals = self.window.currentCoords[0]
        imags = self.window.currentCoords[1]
        realNumerator = (self.window.currentCoords[2] - reals) * self.quality
        imagNumerator = (self.window.currentCoords[3] - imags) * self.quality
        imagStep = imagNumerator/self.window.height
        realStep = realNumerator/self.window.width
        self.window.clear()

        while reals < self.window.currentCoords[2]:
            imags = self.window.currentCoords[1]
            while imags < self.window.currentCoords[3]:
                try:
                    begZ = complex(reals, imags)
                    z = begZ
                    if self.shading:
                        for iterates in range(0,self.iterations):
                            z = self.newton(z)
                            for x in range(0,len(self.roots)):
                                if cmath.isclose(z, self.roots[x], rel_tol = self.reltol):
                                    self.plotZ(begZ, self.getColor(x , iterates))
                                    iterates = self.iterations
                    else:
                        for iterates in range(0, self.iterations):
                            z = self.newton(z)
                        for x in range(0,len(self.roots)):
                            if cmath.isclose(z, self.roots[x], rel_tol = self.reltol):
                                if self.useAlts:
                                    self.plotZ(begZ, self.altcolors[x])
                                else:
                                    self.plotZ(begZ, self.colors[x])
                except OverflowError:
                    print("Overflow at " + str(imags) + " , " + str(reals) + " caught.")
                imags+= imagStep
            reals += realStep

            if self.flushing:
                self.window.update()
        self.window.update()
        print("plot time: " + str(time.time() - startTime) + "s")
