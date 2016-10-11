#!/usr/bin/env python

# test whether a given number n is prime
import numpy

n = 25

# We test in a while loop whether n is divided by
# all numbers from 2 up to the square root.
#
# Explanation:
# divisors of a natural number n always come in pairs:
# n = k * l; Here, one of the numbers of k and l must
# be smaller (equal) to the square root and the other one
# greater (equal) to the square root. If both numbers were
# smaller than the square root of n, the product could not
# be 'n' etc.

# We construct the while loop so that we do not need to
# leave it with a 'break'-statement at some point. I
# stronglz discouverage you ever doing this.
prime = True
i = 2
while (prime == True) and (i <= numpy.sqrt(n)):
    if n%i == 0:
        prime = False
    i = i + 1

if prime == True:
    print("%d is prime" % (n))
else:
    print("%d is not prime" % (n))
