"""
Problem #14

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from random import random
import math

radius = 2

def isInsideCircle(x, y, rs):
    return x**2 + y**2 < rs

def estimate_pi(num_random_tests):
    pi_counter = 0
    rsquared = radius ** 2

    for _ in range(num_random_tests):
        x_rand = random() * radius
        y_rand = random() * radius

        #if(x_rand ** 2) + (y_rand ** 2) < rsquared:
        if isInsideCircle(x_rand, y_rand, rsquared):
            pi_counter += 1

    return 4 * pi_counter / num_random_tests

print("Result: ", round(estimate_pi(100000000),3))
assert round(estimate_pi(100000000),3) == 3.141