from example import main
import numpy as np

# test the delta calculation function
def test_calc_deltas():
    # typical case
    assert main.calc_deltas(np.array([3, 4])) == np.array([-1])
    # same thing as previous but using floats
    assert main.calc_deltas(np.array([3.0, 4.0])) == np.array([-1.0])
    # edge case, only one element
    assert np.size(main.calc_deltas(np.array([3]))) == 0

