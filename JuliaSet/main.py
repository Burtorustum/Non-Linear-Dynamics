#main.py
from MandelbrotSet import *
from JuliaSet import *

def main():
    running = True
    print("This program is for viewing Julia Sets with varying c values as well as the Mandelbrot Set.")
    print("Now loading Mandelbrot Set...")
    mandelbrot = MandelbrotSet(600,600)
    mandelbrot.regPlotSet(maxIterates=50)
    mandelbrot.window.update()
    print("Now loading Julia Set low quality render...")
    julia = JuliaSet(600,600)
    julia.inversePlotSet()
    julia.lqwindow.update()
    julia.hqwindow.update()

    #TODO: Choose point on MandelbrotSet and draw corresponding julia Set,
    #      Color Schemes
    #      Allow user to change num of iterates / quality
    #      Optimize iterate amount based on zoom
    while running:
        None;

if __name__ == '__main__':
    main()
