#FractalTreeMain.py
from FractalTree import FractalTree
from nld_graphics import *
from graphics import *
import math as math
from getOption import getOption

def main():
    window = NLDGraphWin("Fractal Trees", 600, 600, [-5,-5,5,5])
    defaultTree = FractalTree(30, .75, window=window)
    defaultTree.drawTreeRec(6, Point(0,0), 1, math.radians(90))

    trees = [defaultTree]
    animated = True
    colored = True
    randAngle = False
    randLength = False
    scaleWidth = True

    #Idea: thread the drawing of trees so that you could make the program run continuously while they are being drawj
    inp = ''
    commands()
    while inp != 'quit' and inp != 'q' and inp != 'exit':
        inp = str.lower(input(' ~ '))

        if inp == 'animate':
            animated = not animated
            print("Animated tree drawing is currently", ("on." if animated else "off."))

        elif inp == 'color':
            colored = not colored
            print("Colored trees are currently", ("on." if colored else "off."))

        elif inp == 'rand angle':
            randAngle = not randAngle
            print("Randomly angled branches is currently", ("on." if randAngle else "off."))

        elif inp == 'rand length':
            randLength = not randLength
            print("Random length of branches is currently", ("on." if randLength else "off."))

        elif inp == 'width scale':
            scaleWidth = not scaleWidth
            print("Width scaling is currently", ("on." if scaleWidth else "off."))

        elif inp == 'new tree':
            print("Input the angle theta of the tree (in degrees): ")
            angle = int(getOption(0,360))
            print("Input the scale factor of the tree: ")
            scaleFactor = getOption(0,2)
            print("Input the level at which to draw the tree: ")
            level = int(getOption(1,20))
            print("Input the overall direction of the tree (90 is straight up): ")
            direction = getOption(0,360)
            print("Click where you would like to draw the bottom of the tree: ")
            point = window.getMouse()
            trees.append(FractalTree(angle, scaleFactor, window))
            trees[-1].drawTreeRec(level, point, 1, math.radians(direction), colored=colored, animated=animated, randomAngle=randAngle, randomLength=randLength, widthScaling=scaleWidth)
            print()

        elif inp == 'remove tree':
            if len(trees) > 0:
                trees[0].clear()
                del(trees[0])
            else:
                print("No trees currently drawn!")

        elif inp == 'clear':
            trees = []
            window.items = []
            window.clear()

        elif inp == 'commands':
           commands()

        #Look into correction for mistyped commands...
        elif inp != 'quit' and inp != 'q' and inp != 'exit':
            print('That was not a valid command.')


def commands():
    print()
    print("quit / q - Quit the program")
    print("color - Toggle coloring the trees")
    print("animate - Toggle animating new trees")
    print("rand angle - Toggle randomly angled branches")
    print("rand length - Toggle random length branches")
    print("width scale - Toggle width scaling of the branches")
    print("new tree - draw a new tree with input and current settings")
    print("remove tree - removes the oldest drawn tree")
    print("clear - clears the entire window")


if __name__ == '__main__':
    main()
