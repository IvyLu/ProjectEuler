# -*- coding: utf-8 -*-
intro = """
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

def fibonaccisumeven(n):
    sumeven = 0
    first = 0
    second = 1
    nextone = first + second
    while nextone < n:
        first = second
        second = nextone
        nextone = first + second
        
        if nextone % 2 == 0:
            sumeven+=nextone
    
    return sumeven


print intro

print fibonaccisumeven(4000000)