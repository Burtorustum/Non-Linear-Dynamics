#RegularPolygons.py
from math import sin, cos, pi

def genPolygonPoints(numPoints, centerpoint = (0,0), radius = 1)
    vertices = []
    for n in range(numPoints):
        x = (radius * cos(2*pi*n/5) + centerpoint[0])
        y = (radius * sin(2*pi*n/5) + centerpoint[1])
        vertices.append((x, y))
    return vertices
