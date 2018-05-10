#KochMain.py
from KochCurve import *
from getOption import getOption
def main():
    print("Starting...")

    curve = KochCurve(60, 1)
    curve.drawCurve(Point(0,0), 4, 0, 'animated', False)
    level = 4
    inner = False

    inp = ''
    commandList()
    while inp != 'q':

        inp = str.lower(input(' ~ '))
        if inp == 'level':
            level = getOption(0,10)
        elif inp == 'angle':
            curve.setAngle(getOption(0,180))
        elif inp == 'length':
            curve.setLength(getOption(1,5))
        elif inp == 'inner':
            inner = not inner
            print('Polygons will be drawn in the', 'inner style.' if inner else 'outer style.')
        elif inp == 'poly':
            curve.clear()
            curve.drawPolygon(Point(0,0), level, int(getOption(3, 18)), inner)
        elif inp == 'curve':
            curve.clear()
            curve.drawCurve(Point(0,0), level, 0, 'regular', False)
        elif inp == 'help':
            commandList()
        elif inp != 'q':
            print('Whoops! That wasn\'t a valid input.')

        print()

def commandList():
    print()
    print('q = Quit')
    print('level = Change level at which the curves are drawn')
    print('angle = Change the Koch generating angle')
    print('length = Change the length of each individual curve')
    print('inner = Toggle whether Polygons are drawn inner or outer style')
    print('poly = Draw a polygon with a desired number of sides')
    print('curve = Draw a curve with the current settings')
    print('help = Redisplay this list of commands')

if __name__ == '__main__':
    main()
