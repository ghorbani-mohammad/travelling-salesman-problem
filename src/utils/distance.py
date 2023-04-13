from typing import List
from math import sqrt


def euclidean_distance(*points: List[float]) -> float:
    """
    Calculates the Euclidean distance between any number of points.
    """
    if len(points) < 2:
        raise ValueError(
            "At least two points are required to calculate the Euclidean distance."
        )
    distance = 0
    for i in range(len(points) - 1):
        squared_distance = sum(
            (p1 - p2) ** 2 for p1, p2 in zip(points[i], points[i + 1])
        )
        distance += sqrt(squared_distance)
    return distance
