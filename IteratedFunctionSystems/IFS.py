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
    transformOptions = ['r', 's', 'theta', 'phi', 'h', 'k', 'probability']
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
                    if thing == 'phi' or thing == 'probability':
                        print("that was not a valid input. Using None instead.")
                        nextTransformOptions.append(None)
                    else:
                        print("that was not a valid input. Using 0 instead.")
                        nextTransformOptions.append(0)

            transformations.append(TransformationObject(r=nextTransformOptions[0], s=nextTransformOptions[1], theta=nextTransformOptions[2], phi=nextTransformOptions[3], h=nextTransformOptions[4], k=nextTransformOptions[5]))
            nextTransformOptions[:] = []
            print(transformations[-1], '\n')
    pointeroo = (randrange(-1000,1000) / 1000.1,randrange(-1,1) / 1000.1)

    minimumProb = 1
    for transform in transformations:
        if minimumProb > transform.probability:
            minimumProb = transform.probability

    print (minimumProb)
    newTransformations = []
    for transform in transformations:
        transform.probability = 1/minimumProb * transform.probability
        #print(transform.probability)
        for i in range(int(transform.probability)):
            newTransformations.append(transform)
        print(transform)
    transformations = newTransformations

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

    minimum = minX if minX < minY else minY
    maximum = maxX if minimum == minX else maxY
    if minimum == minX:
        while maxX - minX <= maxY - minY:
            maxX += .1
            minX -= .1
        minimum = minX
        maximum = maxX
    else:
        while maxX - minX >= maxY - minY:
            maxY += .1
            minY -= .1
        minimum = minY
        maximum = maxY

    #print(str(minimum) + " " + str(maximum))
    window.setCoords(minimum-.1, minimum-.1, maximum+.1, maximum+.1)

    print("Plotting")
    startime = time.time()
    for x in range(1000000):
        random = randint(0,len(transformations)-1)
        transform = transformations[random]
        pointeroo = transform.apply(pointeroo)
        window.plot(pointeroo[0], pointeroo[1])
        if x % 5000 == 0 and x < 20000:
            window.update()
    print(time.time()-startime)
    print("Done.")

    window.update()
    window.getMouse()
    window.close()

if __name__ == '__main__':
    main()
