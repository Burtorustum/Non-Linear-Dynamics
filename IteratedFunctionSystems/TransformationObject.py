#Transformation.py
from graphics import Point
from math import sin, cos

class TransformationObject:
    def __init__(self, r=1, s=1, theta=0, phi=None, h=0, k=0):
        self.phi = theta if phi == None else phi
        self.r = r
        self.s = s
        self.theta = theta
        self.h = h
        self.k = k

    def transform(self, points):
        transformedPoints = []
        for point in points:
            transformedPoints.append(self.apply(point))
        return transformedPoints

    def apply(self, point):
        x = self.r * cos(self.theta) * point[0] - self.s * sin(self.phi) * point[1] + self.h
        y = self.r * sin(self.theta) * point[0] + self.s * cos(self.phi) * point[1] + self.k

        return (x, y)
