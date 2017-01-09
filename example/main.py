import numpy as np
import scipy as sp

# example useful function
def calc_deltas(x):
    return x[0:-1] - x[1:]

# main function, only called when this file is
# executed from the command line
def main():
    print("This is the main function")

    x = sp.rand(10)
    print(x)
    print("Deltas: {0}".format(calc_deltas(x)))

# if run from the command line
if __name__ == "__main__":
    main()
