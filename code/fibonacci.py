#!/usr/bin/env python3

# calculate the sum of the first 1000 Fibonacci numbers

fib_sum = 0  # the sum of the umbers
fib_n = 1    # the nth Fib. number
fib_np1 = 1  # the nth+1 Fib. number

n = 1000
i = 1
while i <= n:
    fib_sum = fib_sum + fib_n

    # The following way to obtain the next
    # Fib. number with a temporary variable is
    # the way from classical languages.
    #
    # In python the follwing three code lines
    # could be replaced by the single line:
    # fib_n, fib_np1 = fib_np1, fib_n + fib_np1
    tmp = fib_n
    fib_n = fib_np1
    fib_np1 = tmp + fib_n
    i = i + 1
    
print("The sum of the first %d Fib. numbers is %d:" % (n, fib_sum))
