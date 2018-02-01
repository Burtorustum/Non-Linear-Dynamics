from graphics import Point
from math import sin, cos

class Transformation:
    def __init__(self, r=1, s=1, theta=0, phi=None, h=0, k=0):
        phi = theta if phi == None else phi
        self.r = r
        self.s = s
        self.theta = theta
        self.phi = phi
        self.h = h
        self.k = k

    def transform(self, points):
        transformedPoints = []
        for point in points:
            transformedPoints.append(apply(point))
        return transformedPoints

    def apply(self, point):
        x = self.r * cos(self.theta) * point.x - self.s * sin(self.phi) * point.y + self.h
        y = self.r * sin(self.theta) * point.x + self.s * cos(self.phi) * point.y + self.k

        return Point(x, y)
