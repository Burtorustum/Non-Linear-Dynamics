#getOption.py -- Robert Aburustum
from math import pi
def getOption(i,n):
    x = n+1
    while x <= i or x >= n:
        try:
            x = float(eval(input("Please input a number between " + str(i) + " and " + str(n) + " exclusive. \n")))
        except ValueError:
            print("That's not a number.")
            x = n+1
        except SyntaxError:
            print("There is a problem in your input syntax")
            x = n+1
    return x
