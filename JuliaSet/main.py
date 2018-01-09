#main.py
from MandelbrotSet import *
from JuliaSet import *

def main():
    running = True
    print("This program is for viewing Julia Sets with varying c values as well as the Mandelbrot Set.\n")
    print("Now loading Mandelbrot Set...")
    mandelbrot = MandelbrotSet(600,600)
    mandelbrot.regPlotSet(maxIterates=50)
    mandelbrot.window.update()
    print("Now loading a Julia Set low quality render...")
    julia = JuliaSet(600,600)
    julia.inversePlotSet()
    julia.lqwindow.update()
    julia.hqwindow.update()

    #TODO:
    #      Choose point on MandelbrotSet and draw corresponding julia Set
    #      Manually input a c value
    #      Multiple color schemes?
    #      Allow user to change num of iterates / quality
    #      Optimize iterate amount based on zoom
    while running:
        print("\nChoose a point on the Mandelbrot Set")
        point = mandelbrot.window.getMouse()
        julia.lqwindow.clear()
        julia.inversePlotSet(const=complex(point.x, point.y))
        inp = input("Would you like to draw a high quality render of the point " + str(complex(point.x, point.y)) + " ? y/n \n")
        if inp == 'y':
            julia.hqwindow.clear()
            julia.regPlotSet(const = complex(point.x, point.y))



if __name__ == '__main__':
    main()
