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
    transformations = []
    transformOptions = ['r', 's', 'theta', 'phi', 'h', 'k']
    nextTransformOptions = []
    gettingIn = True

    inp = ""
    while (gettingIn):
        inp = input("Enter 'e' to end the input sequence. Otherwise enter a transformations. 'd' will give a default transformation set. ")
        if (inp.lower() == 'e' and len(transformations) != 0):
            gettingIn = False
        elif (inp.lower() == 'd'):
            transformations = [t1, t2, t3]
            gettingIn = False
        else:
            for thing in transformOptions:
                inp = input("Enter a value for " + thing + ": ")
                try:
                    x = eval(inp)
                    nextTransformOptions.append(x)
                except:
                    print("that was not a valid input. Using 0 instead.")

            transformations.append(TransformationObject(r=nextTransformOptions[0], s=nextTransformOptions[1], theta=nextTransformOptions[2], phi=nextTransformOptions[3], h=nextTransformOptions[4], k=nextTransformOptions[5]))
            nextTransformOptions[:] = []
            print(transformations[-1], '\n')
    pointeroo = (.5,.5)
    for transform in transformations:
        print(transform)

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
    for x in range(100000):
        random = randint(0,len(transformations)-1)
        transform = transformations[random]
        pointeroo = transform.apply(pointeroo)
        window.plot(pointeroo[0], pointeroo[1])
        if x % 5000 == 0:
            window.update()
    print(time.time()-startime)
    print("Done.")

    window.update()
    window.getMouse()
    window.close()

if __name__ == '__main__':
    main()
