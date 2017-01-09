import numpy as np
import scipy as sp
from .utils import gen_rand_sym_mat

# example useful function
def calc_deltas(x):
    return x[0:-1] - x[1:]

# do things
def run():
    print("This is the main function")

    x = sp.rand(10)
    print(x)
    print("Deltas: {0}".format(calc_deltas(x)))

    print("\nGenerate random symmetric matrix")
    print(gen_rand_sym_mat(3))
