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
    A = (triangle_coordinates[0:0], triangle_coordinates[1:0])
    B = (triangle_coordinates[0:1], triangle_coordinates[1:1])
    C = (triangle_coordinates[0:2], triangle_coordinates[1:2])
    P = point_coordinates
    v0 = (B[0] - A[0], B[1] - A[1])
    v1 = (C[0] - A[0], C[1] - A[1])
    v2 = (P[0] - A[0], P[1] - A[1])
    dot00 = v0[0]*v0[0] + v0[1]*v0[1]
    dot01 = v0[0]*v1[0] + v0[1]*v1[1]
    dot02 = v0[0]*v2[0] + v0[1]*v2[1]
    dot11 = v0[0]*v1[0] + v1[1]*v1[1]
    dot12 = v0[0]*v2[0] + v1[1]*v2[1]
    inv_denom = 1/(dot00*dot11 - dot01*dot01)
    u = (dot11*dot02 - dot01*dot12)*inv_denom
    v = (dot00*dot12 - dot01*dot02)*inv_denom
    return (u >= 0) and (v >= 0) and (u + v <= 1)