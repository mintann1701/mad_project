#Question 2 - left_endpoint function
#left_endpoint function
import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    width = np.diff(x_vals)
    height = func((x_vals[:-1]))
    return np.sum(width * height)

#simpson function
def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    a = x_vals[0]
    b = x_vals[-1]
    mid_point = (a + b) / 2
    calculate_integral = ((b-a)/6) * (func(a) + func(b) + 4*func(mid_point))
    return calculate_integral

