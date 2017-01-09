import numpy as np

def gen_rand_mat(N):
    """
    Generates a random symmetric 2D matrix of size `N` pulling from the
    uniform distribution on ``[0, 1)``
    """

    mat = np.random.rand(N, N)
    return np.tril(mat) + np.tril(mat, -1).T
