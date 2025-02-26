from operator import truediv

import numpy as np

def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    """
    Calculates the barycentric coordinates of a point with respect to a triangle. Creates a 2x3 array of the coordinates
    and returns a 1d array with the values of lambda.

    """
    # Extract triangle vertex coordinates correctly
    x1, x2, x3 = triangle_coordinates[0, :]
    y1, y2, y3 = triangle_coordinates[1, :]

    # Extract point coordinates
    x, y = point_coordinates

    # Calculate denominator
    denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)

    # Calculate lambda 1
    lambda1 = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator

    # Calculate lambda 2
    lambda2 = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator

    # Calculate lambda 3
    lambda3 = 1 - lambda1 - lambda2


    # Return barycentric coordinates as a numpy array
    return np.array([lambda1, lambda2, lambda3])


def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    """
    The barycentric coordinates is a 1x3 NumPy array representing (lambda1, lambda2, lambda3
    We want to convert barycentric coordinates to Cartesian coordinates
    """
    barycentric_coordinates = np.dot(triangle_coordinates, barycentric_coordinates)
    return np.array(barycentric_coordinates)

def is_inside_triangle(triangle_coordinates, point_coordinates):
    """
    Calculates whether each lambda is positive. If they are all positive,
    then the point must be inside the triangle.
    """
    lambda1 = get_barycentric_coordinates(triangle_coordinates,point_coordinates)[0]
    lambda2 = get_barycentric_coordinates(triangle_coordinates,point_coordinates)[1]
    lambda3 = get_barycentric_coordinates(triangle_coordinates,point_coordinates)[2]
    return lambda1 > 0 and lambda2 > 0 and lambda3 > 0