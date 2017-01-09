import numpy as np
from example import utils

def test_gen_rand_sym_mat():
    np.random.seed(0)
    utils.gen_rand_sym_mat(3) == np.array([
        [ 0.5488135 ,  0.54488318, 0.43758721], 
        [ 0.54488318,  0.4236548 ,  0.891773  ], 
        [ 0.43758721,  0.891773  ,  0.96366276]
        ])
