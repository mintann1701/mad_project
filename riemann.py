#Question 2
#left_endpoint function
import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    width = np.diff(x_vals)
    height = func((x_vals[:-1]))
    return np.sum(width * height)
