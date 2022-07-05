#!/usr/bin/python3
"""Creating Pascal triangle function"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Returns: a list of list of integers
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangle[-1]
        tmp = [1]
        for z in range(len(tri) - 1):
            tmp.append(tri[z] + try[z + 1])
        tmp.append(1)
        triangles.append(tmp)
    retun triangles
