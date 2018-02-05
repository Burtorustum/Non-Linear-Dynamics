#IFS.py
from nld_graphics import *
from graphics import *
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("IFS", "Utility")
sys.path.insert(0, path)
from random import randint
import time
from TransformationObject import *

window = NLDGraphWin("IFS", 800, 800, [-1,-1,1,1])
def main():
    t1 = TransformationObject(r=.5, s=.5)
    t2 = TransformationObject(r=.5, s=.5,h=.5)
    t3 = TransformationObject(r=.5, s=.5,k=.5)
    transformations = [t1, t2, t3]
    pointeroo = Point(1, 1)

    for x in range(1000000):
        random = randint(0,2)
        transform = transformations[random]
        pointeroo = transform.apply(pointeroo)

    for x in range(100000):
        random = randint(0,2)
        transform = transformations[random]
        pointeroo = transform.apply(pointeroo)
        window.plot(pointeroo.x, pointeroo.y)
        if x % 3000 == 0:
            window.update()

    window.update()
    window.getMouse()
    window.close()

if __name__ == '__main__':
    main()
