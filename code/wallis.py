#!/usr/bin/env python3

import numpy

# estimate pi with the indefinite, very slowly converging,
# Wallis product.
pi_real = 3.141592653589793238462643383279

# we evaluate the product by keeping (arbitraily exact)
# integer arithmetic as long as possible
n = 20000  # number of Wallis product element that we want
           # to consider
num = 1    # holds the numerator
denom = 1  # holds the denominator

i = 1
while i <= n:
    tmp = 4 * i**2
    num = num * tmp
    denom = denom * (tmp - 1)
    i = i + 1

# only here we do a conversion to float:
pi_approx = (2 * num) / denom

# absolute and relative error:
err_abs = numpy.abs(pi_real - pi_approx)
err_rel = numpy.abs(pi_real - pi_approx) / pi_real

print("Absolute error with %d elements: %f" % (n, err_abs))
print("Relative error with %d elements: %f" % (n, err_rel))

