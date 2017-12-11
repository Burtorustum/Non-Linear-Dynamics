#getOption.py -- Robert Aburustum
def getOption(i,n):
    x = n+1
    while x <= i or x >= n:
        try:
            x = float(input("Please input a number between " + str(i) + " and " + str(n) + " exclusive. \n"))
        except ValueError:
            print("That's not a number.")
            x = n+1
    return x

def main():
        getOption(0,3)
        print("good job.")

if __name__ == "__main__":
    main()
