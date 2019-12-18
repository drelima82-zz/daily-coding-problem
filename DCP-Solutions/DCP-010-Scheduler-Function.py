# Problem #10

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def any_function():
    print("andre")

def scheduler(f, time_to_wait):
    time.sleep(time_to_wait / 1000)   # Delays for 5 seconds. You can also use a float value.
    f()

scheduler(any_function, 5000)