#IFS.py
from nld_graphics import *
from graphics import *
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("IFS", "Utility")
sys.path.insert(0, path)
from random import randint, randrange
import time
from TransformationObject import *

window = NLDGraphWin("IFS", 800, 800, [-1,-1,1,1])
def main():
    t1 = TransformationObject(r=.5, s=.5)
    t2 = TransformationObject(r=.5, s=.5, h=.5, theta=45)
    t3 = TransformationObject(r=.5, s=.5, k=.5)

    transformations = [t1, t2, t3]
    pointeroo = (randrange(-1,1),randrange(-1,1))

    random = randint(0,len(transformations)-1)
    transform = transformations[random]
    pointeroo = transform.apply(pointeroo)

    minX = pointeroo[0]
    minY = pointeroo[1]
    maxX = pointeroo[0]
    maxY = pointeroo[1]

    print("Transients")
    for x in range(1000000):
        random = randint(0,len(transformations)-1)
        transform = transformations[random]
        pointeroo = transform.apply(pointeroo)

        if pointeroo[0] > maxX:
            maxX  = pointeroo[0]
        elif pointeroo[0] < minX:
            minX = pointeroo[0]

        if pointeroo[1] > maxY:
            maxY = pointeroo[1]
        elif pointeroo[1] < minY:
            minY = pointeroo[1]


    if maxX - minX > maxY - minY:
        window.setCoords(minX - .1, minX - .1, maxX + .1, maxX + .1)
    else:
        window.setCoords(minY - .1, minY - .1, maxY + .1, maxY + .1)

    print("Plotting")
    startime = time.time()
    for x in range(250000):
        random = randint(0,len(transformations)-1)
        transform = transformations[random]
        pointeroo = transform.apply(pointeroo)
        window.plot(pointeroo[0], pointeroo[1])
        if x % 10000 == 0:
            window.update()
    print(time.time()-startime)

    window.update()
    window.getMouse()
    window.close()

if __name__ == '__main__':
    main()
