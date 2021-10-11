import numpy as np
import pandas as pd

from scipy.ndimage import gaussian_filter
from scipy import misc

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'my_concat']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
 return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def my_concat(A, B, C=None):
    try:
        return pd.concat([A, B, C])
    except TypeError:
        return pd.concat([A, B])
