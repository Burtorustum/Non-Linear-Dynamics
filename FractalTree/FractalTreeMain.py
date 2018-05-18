#FractalTreeMain.py
from FractalTree import FractalTree
from nld_graphics import *
from graphics import *
import math as math
from getOption import getOption

def main():
    window = NLDGraphWin("Fractal Tree", 600, 600, [-5,-5,5,5])
    defaultTree = FractalTree(30, .75, window=window)
    defaultTree.drawTreeRec(6, Point(0,0), 1, math.radians(90))

    inp = ''
    while inp != 'quit' and inp != 'q':
        inp = str.lower(input(' ~ '))

if __name__ == '__main__':
    main()
