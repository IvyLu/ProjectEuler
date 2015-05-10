print """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import Counter

def prime_factor_list(n):
    i=2
    factor_list = []
    while i * i <= n:
        while n % i == 0:
            if n==i:
                factor_list.append(i)
                return factor_list
            n = n / i
            factor_list.append(i)
        i = i + 1
    
    factor_list.append(n)
    return factor_list

#print prime_factor_list(20)
    

def small_common_multiple(a,b):
    list_a = prime_factor_list(a)
    list_b = prime_factor_list(b)
    intersect = list((Counter(list_a) & Counter(list_b)).elements())
    
    temp = 1
    for i in intersect:
        temp = temp * i
    
    largest_common_factor = temp
    
    return a*b/largest_common_factor
    
#print small_common_multiple(4,6)


def smallest_multiple(n):
    mul = 1
    for i in range(1,n+1):
        mul = small_common_multiple(i,mul)
        
    return mul
    
print smallest_multiple(20)