#!/usr/bin/env python3

# estimate the square root with Herons mathod

# we need numpy for the abs-function
import numpy

# From that number we want to estimate the square root:
x = 5987.1234

# current estimate for the square root:
y_curr = 1.0

# new estimate after a Heron iteration; we need to set it here to some
# value so that we can enter the while loop
y_new = y_curr + 1.0

# The while loops iterates until consecutive
# estimates for the square root differ by less than
# epsilon. We also save the number of iterations
# we need to achieve this (this was not part of the
# exercise):
iterations = 0
while numpy.abs(y_new - y_curr) > 1.0e-06:
    y_curr = y_new
    y_new = 0.5 * (y_curr + (x / y_curr))
    iterations = iterations + 1
    
print("Final square root estimate for %f after %d iterations: %f" %
      (x, iterations, y_new))
print("Square of the square-root estimate: %f" % (y_new**2))
