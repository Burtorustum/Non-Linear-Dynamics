#Transformation.py
from graphics import Point
from math import sin, cos, pi

class TransformationObject:
    def __init__(self, r=1, s=1, theta=0, phi=None, h=0, k=0, probability=None):
        self.probability = abs(r * s) if probability == None or r != s else probability
        self.phiDeg = theta if phi == None else phi
        self.thetaDeg = theta
        self.r = r
        self.s = s
        self.theta = theta * pi/180
        self.phi = self.phiDeg * pi/180
        self.h = h
        self.k = k

    def changeTransform(self, r=1, s=1, theta=0, phi=None, h=0, k=0, probability=None):
        self.probability = r if probability == None else probability
        self.phiDeg = theta if phi == None else phi
        self.thetaDeg = theta
        self.r = r
        self.s = s
        self.theta = theta * pi/180
        self.phi = self.phiDeg * pi/180
        self.h = h
        self.k = k

    def apply(self, point):
        x = self.r * cos(self.theta) * point[0] - self.s * sin(self.phi) * point[1] + self.h
        y = self.r * sin(self.theta) * point[0] + self.s * cos(self.phi) * point[1] + self.k
        return (x, y)

    def strToVals(self, string):
        strArr = string.split("|")
        strArr.pop(-1)
        strArr.pop(0)
        newTransforms = []

        for part in strArr:
            nexty = part.split(": ")[1]
            newTransforms.append(nexty)

        newTransforms = [float(eval(newTransforms[0])), float(eval(newTransforms[1])), float(eval(newTransforms[2])), float(eval(newTransforms[3])), float(eval(newTransforms[4])), float(eval(newTransforms[5]))]
        self.changeTransform(newTransforms[0], newTransforms[1], newTransforms[2], newTransforms[3], newTransforms[4], newTransforms[5])

    def __str__(self):
        return "|r: " + str(self.r) + "|s: " + str(self.s) + "|theta: " + str(self.thetaDeg) + "|phi: " + str(self.phiDeg) + "|h: " + str(self.h) + "|k: " + str(self.k) + "|Probability: " + str(self.probability) + "|"
