import numpy as np

def gen_rand_sym_mat(N):
    """
    Generate a random symmetric 2D matrix of size `N`x`N` from a uniform
    distribution on the interval ``[0, 1)``.
    """
    mat = np.random.rand(N, N)
    return np.tril(mat) + np.tril(mat, -1).T
