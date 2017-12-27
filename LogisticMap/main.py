#main.py
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("LogisticMap", "Utility")
sys.path.insert(0, path)
from BifurcationDiagram import BifurcationDiagram
from CobwebDiagram import CobwebDiagram
from getOption import *

def main():
    print("This is a program for viewing the Bifurcation Diagram and Cobweb Diagram of the LogisticMap in particular, however, it can be adapted to work with other functions. Please wait while the initial graphs are drawn.")
    running = True
    bifurcationWin = BifurcationDiagram(flush = False)
    cobwebWin = CobwebDiagram()
    bifurcationWin.flushing = True

    print ("If you need help at anytime, enter 'commands' to view the available commands.")
    while running:
        inp = input("Enter a command! ")
        inp = inp.lower()

        #If sequence to test for different inputs
        if inp == "q":
            running = False

        elif inp == "commands":
            print("\nCommands for the biurcation diagram include:\nzoom - input 2 values to change your horizontal coordinates to. \nclickzoom - click to zoom! \ntwoclickzoom - Click in two spots, one to the left and one to the right and see that area")
            print("zoomout - zoom to the original coordinates \nbiftransients - change the number of transients lost before graphing the diagram and regraph")
            print("\nCommands for the cobweb diagram inlude: \nchanger - change the r value of the map \nchangex - change the initial x value of the map")
            print("cobiterates - change the number of iterates shown in the diagram")
            print("\nIf you would like to quit, enter 'q'.\n")

        elif inp == "zoom":
            x1 = getOption(0,4)
            x2 = getOption(0,4)
            if x1 < x2:
                bifurcationWin.coords[0] = x1
                bifurcationWin.coords[2] = x2
            else:
                bifurcationWin.coords[0] = x2
                bifurcationWin.coords[2] = x1

            bifurcationWin.zoom()

        elif inp == "clickzoom":
            print("click on the bifurcation diagram window!")
            bifurcationWin.oneClickZoom()

        elif inp == "twoclickzoom":
            print("click on the bifurcation diagram window in two places!")
            bifurcationWin.twoClickZoom()

        elif inp == "zoomout":
            bifurcationWin.zoomout()

        elif inp == "biftransients":
            bifurcationWin.drawBifurcationDiagram(numTransients = int(getOption(1,100000)))

        elif inp == "changer":
            cobwebWin.setR(getOption(0,4))

        elif inp == "changex":
            cobwebWin.setx0(getOption(0,1))

        elif inp == "cobiterates":
            cobwebWin.drawCobwebDiagram(iterates = int(getOption(1,1000)))


if __name__ == '__main__':
    main()
