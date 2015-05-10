# -*- coding: utf-8 -*-
intro = """
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def ispalindrome(s):
    s = str(s)
    n = len(s)/2
    for i in range(n):
        if s[i]!=s[len(s)-1-i]:
            return False
    
    return True

def largepalindrome():
    for n in range(999*999,100*100,-1):
        if ispalindrome(n):
            for i in range(999,100,-1):
                if n%i==0 and len(str(n/i))==3:
                    print i,n/i
                    return n
            
 
print intro

print largepalindrome()