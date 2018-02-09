import math
import random


def circle_area(radius):
    """
    Calculates the area of a circle with given radius.
    radius: non-negative float
    Returns: float
    """
    area = math.pi*(radius**2)
    return area
def is_even(number):
    """
    Checks if number is even
    number: integer
    Returns: True if number is even, False otherwise
    

    """
    remander = number%2
    if remander == 0:
        return True
    else:
        return False    