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

 def sum_of_odd_to(n):
    """
    Calculates the sum of all odd numbers 
    from 1 to given n
    n: positive integer
    Returns: integer
    """
    odd_sum = 0
    for odd in range(1,n+1,2):
        
        odd_sum += odd
    return odd_sum
 def miles_per_gallon(miles, gallons):
    """
    Calculates miles per gallons
    miles: positive float
    gallons: positive float
    """
    if (gallons > 0):
        mpg = miles/gallons
        return mpg
def ten_random_numbers(start, stop):
    """
    Prints ten random integers between start and stop
    """
    if start <= stop:
        for i in range(10):

            random_int = random.randint(start,stop)
            print(random_int)