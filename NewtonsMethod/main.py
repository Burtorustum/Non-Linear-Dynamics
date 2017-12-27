#main.py
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("LogisticMap", "Utility")
sys.path.insert(0, path)
from NewtonsMethod import NewtonsMethod
from sympy import *
from math import pi
from getOption import *

def main():
    z = symbols('z')

    print("\nThis program is for viewing the effects of running Newton's method on polynomials in the complex plane. Please wait while the inital function is drawn (z**3-1)")
    running = True
    window = NewtonsMethod(func=z**3-1, sym=z, coords=[-1,-1,1,1])
    window.quality = 1.3
    window.draw()
    print("If you need a list of commands type, 'commands'. To quit, type 'quit'.")
    while running:
        inp = input("\nPlease input a command. If you need a list of commands type, 'commands'.\n")

        if inp == 'quit' or inp =='q':
            running = False

        elif inp == 'commands':
            print("\nCommands: ")
            print("*'function' - allows you to enter a function in terms of z. Updates the roots and derivative for you. Note: you MUST enter functions in python notation. (i.e. z**4-1 not z^4-1)")
            print("*'zoom' - zoom in on a portion of the plot")
            print("*'zoomout' - zoom out to the original coordinates of the plot")
            print("*'iterates' - change the number of iterates the program will attempt to find the roots")
            print("*'roots' - view the roots the algorithm generated for your function")
            print("*'changeroots' - manually input the roots of a function")
            print("*'viewshades' - choose whether or not shading is enabled on the plot. When enabled drawing takes VERY LONG -- Note: Not working very well right now.")
            print("*'changecoords' - update the default coords of the plot")
            print("*'coolfunctions' - lists some cool functions I have found")
            print("*'colflush' - toggle whether the plot is drawn in columns or all at once")
            print("*'reltol' - change the relative tolerance of the isclose() function")
            print("*'quality' - change the quality of the plot between 'high', 'med' and 'low'. lower quality --> faster draw times")
            print("*'colorscheme' - toggle to a different color scheme. Note: currently only works with functions with up to 7 roots")
            print("*'optimizeiterates' - run a function to attempt to find the optimal number of iterates")
            print("*'redraw' - redraws the plot with your new configuration of settings\n")

        elif inp == 'function':
            try:
                inFunc = eval(input("Please input a function in python notation in the variable 'z'\n"))
                window.updateFunc(function=inFunc, symbol=z)
                if window.roots == []:
                    print("WARNING: ROOTS NOT SUCCESSFULLY FOUND FOR THIS FUNCTION\n")
                else:
                    print("Roots identified:", window.roots)
            except NameError:
                print("Make sure you are using the variable z.")
            except SyntaxError:
                print("There was an error in the syntax of your function")

        elif inp == 'zoom':
            window.window.zoom()
            print("drawing")
            window.draw()

        elif inp == 'zoomout':
            window.window.zoom(whichWay="out")
            print("drawing")
            window.draw()

        elif inp == 'iterates':
            window.iterations = int(getOption(1,1000))

        elif inp == 'roots':
            print(window.roots)

        elif inp == 'changeroots':
            newRoots = []
            rootIn = None
            while rootIn != 'done':
                try:
                    rootIn = input("Input a root in python terms (i.e. 1+1j for the complex value 1 + i). Type 'done' when done\n")
                    newRoots.append(eval(rootIn))
                except SyntaxError and NameError:
                    if rootIn != 'done':
                        print("There was something wrong with your input. Please try again.")

            rootIn = input("Your new roots are: " + str(newRoots) + " Would you like to keep them? y/n? ")
            if rootIn == 'y':
                window.roots = newRoots

        elif inp == 'viewshades':
            window.shading = not window.shading
            print("Toggled shading to", window.shading, "WARNING: VERY SLOW AND LACKLUSTER")

        elif inp == 'redraw':
            print("Drawing. This may take a moment.")
            window.draw()

        elif inp == 'changecoords':
            print("x min:")
            xMin = getOption(-100,100)
            print("x max:")
            xMax = getOption(-100,100)
            print("y min:")
            yMin = getOption(-100,100)
            print("y max:")
            yMax = getOption(-100,100)
            window.window.defaultCoords = [xMin, yMin, xMax, yMax]

        #MAKE INTO SELECTABLE LIST
        elif inp == 'coolfunctions':
            print("7*z**6 - 3*z**3 + 2")
            print("35*z**9 - 180*z**7 + 378*z**5 - 420*z**3 + 315*z")
            print("z**3 - 2*z + 2")
            print("z**8 + 15*z**4 - 16")
            print("z**6 + z**3 - 1")

        elif inp == 'colflush':
            window.flushing = not window.flushing
            print("Toggled colflush to", window.flushing)

        elif inp == 'reltol':
            newtol = getOption(0,1)
            window.reltol = newtol

        elif inp == 'quality':
            qualIn = input("'low,', 'med', or 'high'?\n")
            if qualIn == 'low':
                window.quality = 3
            elif qualIn == 'med':
                window.quality = 1.3
            elif qualIn == 'high':
                window.quality = 1
            print("Changed quality to", qualIn)

        elif inp == 'colorscheme':
            window.useAlts = not window.useAlts
            print("Toggled alternate colorscheme to", window.useAlts)

        elif inp == 'optimizeiterates':
            print("Attempting optimization. This may take a moment.")
            newIterate = window.optimizeIterates()
            if newIterate == window.iterations:
                None
            else:
                inn = input("Would you like to keep the new iterate value, " + str(newIterate) + " y/n? ")
                if inn == 'y':
                    window.iterations = newIterate

        #ADD CHANGE RESOLUTION

if __name__ == '__main__':
    main()
