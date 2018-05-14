#FractalTreeMain.py
from FractalTree import FractalTree
from graphics import *
import math as math

def main():
    tree = FractalTree(90, .75)

    tree.drawTreeRec(13, Point(0,0), 1, math.radians(90), colored=True, animated=False, leftFactor=1, rightFactor=1, assymetricLevel=0, widthScaling=False, width=3)

    tree.window.getMouse()
    tree.window.close()

if __name__ == '__main__':
    main()
