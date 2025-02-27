#Question 2
# These functions below will approximate the Riemann Integrals
#left_endpoint function
import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    This left_endpoint function is used to approximate an integral using the left end point method:

    Parameters
    __________

    x_vals: np.ndarray => A one-dimensional array of x values used to approximate the integral
    func: np.ufunc => The function to approximate the integral of. In this method, we want to calculate
    all the values but the last ([:-1])

    Returns
    Return the left-endpoint sum of the given interval => Approximate the integral
    """
    width = np.diff(x_vals)
    height = func((x_vals[:-1]))
    return np.sum(width * height)

#trapezoid function
def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Computes the integral of a given function using the trapezoidal rule.

    x_vals: A NumPy array of x-values at which the function is evaluated.
            The values should be sorted in ascending order and represent
            the intervals over which integration is performed.
   func: A NumPy universal function that takes an array of x-values
            and returns the corresponding function values.
    Returns the approximated integral of the function over the given x-values using
             the trapezoidal rule.
    """
    dx = np.diff(x_vals)
    fvalues = func(x_vals)
    return np.sum((fvalues[:-1] + fvalues[1:]) / 2 * dx)

#simpson function
def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    This function is used to approximate an integral using the Simpson method:

    Parameters
    __________

    x_vals: np.ndarray => In this method, we consider the middle points and first and last values
    func: np.ufunc => The function to approximate the integral of

    Returns
    _______
    Return the approximate integral of the function over the interval given

     """
    a = x_vals[0]
    b = x_vals[-1]
    mid_point = (a + b) / 2
    calculate_integral = ((b-a)/6) * (func(a) + func(b)+ 4*func(mid_point))
    return calculate_integral



