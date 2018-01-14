#main.py
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("JuliaSet", "Utility")
sys.path.insert(0, path)
from getOption import *
from MandelbrotSet import *
from JuliaSet import *

def main():
    running = True
    print("This program is for viewing Julia Sets with varying c values as well as the Mandelbrot Set.\n")
    print("Now loading Mandelbrot Set...")
    mandelbrot = MandelbrotSet(600,600)
    mandelbrot.regPlotSet()
    mandelbrot.window.update()
    print("Now loading a Julia Set low quality render...")
    julia = JuliaSet(600,600)
    julia.inversePlotSet()
    julia.lqwindow.update()
    julia.hqwindow.update()

    constant = .365 - 0.37j

    #TODO:
    #      Manually input a c value
    #      Multiple color schemes?
    #      Allow user to change num of iterates / quality
    #      Optimize iterate amount based on zoom
    while running:
        print("1. Click a point on the Mandelbrot Set and draw the corresponding Julia Set.")
        print("2. Manually input a c value and draw it.")
        print("3. Manually input the number of iterates to run the Julia Set HQ for.")
        print("4. Manually input the number of iterates to run the Mandelbrot Set for.")
        print("5. Zoom in on the HQ Julia Set.")
        print("6. Zoom out on the HQ Julia Set")
        print("7. Zoom in on the Mandelbrot Set.")
        print("8. Zoom out on the Mandelbrot Set")

        inp = input("Choose an option from the list... ")
        if inp == '0':
            running = False
        elif inp == '1':
            constant = choosePoint(julia=julia, mandelbrot=mandelbrot)
        elif inp == '2':
            constant = inputC(julia=julia)
        elif inp == '3':
            julia.maxIterates = int(getOption(1, 100000))
            julia.hqwindow.clear()
            julia.regPlotSet(const=constant)
        elif inp == '4':
            mandelbrot.maxIterates = int(getOption(1, 100000))
            mandelbrot.window.clear()
            mandelbrot.regPlotSet()
        elif inp == '5':
            julia.zoom(inout="in", constan = constant)
        elif inp == '6':
            julia.zoom(inout="out", constan = constant)
        elif inp == '7':
            mandelbrot.zoom(inout="in")
        elif inp == '8':
            mandelbrot.zoom(inout="out")

    print("All done.")


def choosePoint(julia, mandelbrot):
    print("\nChoose a point on the Mandelbrot Set")
    point = mandelbrot.window.getMouse()
    julia.lqwindow.clear()
    julia.inversePlotSet(const=complex(point.x, point.y))
    inp = input("Would you like to draw a high quality render of the point " + str(complex(point.x, point.y)) + "? (y/n) ")
    if inp == 'y':
        julia.hqwindow.clear()
        julia.regPlotSet(const=complex(point.x, point.y))
        return complex(point.x, point.y)

def inputC(julia):
    invalid = True
    while invalid:
        newC = input("Input a 'c' value for the Julia Set in Python syntax. (ex. .365 - 0.37j)\n")
        try:
            constant = eval(newC)
            invalid = False
        except:
            print("Try again please.")
    julia.lqwindow.clear()
    julia.inversePlotSet(const=constant)
    inp = input("Would you like to draw a high quality render of the point " + str(constant) + "? (y/n) ")
    if inp == 'y':
        julia.hqwindow.clear()
        julia.regPlotSet(const=constant)
        return constant


if __name__ == '__main__':
    main()
