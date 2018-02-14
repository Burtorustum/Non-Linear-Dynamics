#Transformation.py
from graphics import Point
from math import sin, cos, pi

class TransformationObject:
    def __init__(self, r=1, s=1, theta=0, phi=None, h=0, k=0, probability=None):
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
        return None

    def __str__(self):
        return "| r: " + str(self.r) + " | s: " + str(self.s) + " | theta: " + str(self.thetaDeg) + " | phi: " + str(self.phiDeg) + " | h: " + str(self.h) + " | k: " + str(self.k) + " | probabiliy: " + str(self.probability) + " |"
