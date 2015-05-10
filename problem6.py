# -*- coding: utf-8 -*-
intro = """
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.
"""

def sum_sq_difference(n):
    sq_sum = 0
    sum_sq = 0
    for i in range(1,n+1):
        sq_sum += i*i
        sum_sq += i
    
    return sum_sq*sum_sq - sq_sum


print intro
print sum_sq_difference(100)