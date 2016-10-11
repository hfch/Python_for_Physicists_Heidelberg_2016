#!/usr/bin/env python3

# How can we buy 'N" nuggets in chunks of three
# different package sizes.
#
# idea: We use a brute-firce method which cheks
# in three nestes while loops, whether there exits
# one (or more) combinations of three integer numbers
# (i, j, k) such that
# N = N1 * i + N2 * j + N3 * k

# package sizes
N1 = 6
N2 = 9
N3 = 20

# The number of nuggets we want to buy:
N = 60

# will be set to True if we can buy the
# nuggets in one or more combinations:
bought = False

# In the following while statements, the '//'
# operator performs "true integer arithmetic",
# i.e. the division of two ints remains an int
# (cutting away possible fractions - NO ROUNDING)
i = 0
while i <= N // N1:
    j = 0
    while j <= N // N2:
        k = 0
        while k <= N // N3:
            if i * N1 + j * N2 + k * N3 == N:
                print("N = %d: (%d x %d, %d x %d, %d x %d)" %
                      (N, k, N3, j, N2, i, N1))
                bought = True
            k = k + 1
        j = j + 1
    i = i + 1

if bought == False:
    print("N = %d nuggets cannot be bought!" % (N))
