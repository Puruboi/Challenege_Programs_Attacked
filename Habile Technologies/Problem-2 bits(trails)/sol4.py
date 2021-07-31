# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:16:27 2021

@author: PURUBOI
"""
from math import floor

def withMiddleElement(s):

    s = list(s)
    n = floor(len(s)/2)
    
    i=0
    d ,k ,e = n ,1 ,(n-1)
    
    # BASE CASE
    
    s[n - i],s[n + i] = (s[n + i]),(s[n - i])
    s[n - i],s[n + i] = (" " + s[n + i] + " "),(" " + s[n - i] + " ")
    print(''.join(s))
    s = list((''.join(s)))
    
    # Iterative Adding space and Swaping
    
    while k<d:
        i = 0
        n = floor(len(s)/2)
        c = n - e
        while i < c:
            s[n - i],s[n + i] = (s[n + i]),(s[n - i])
            i += 1
        s[n - i],s[n + i] = (" " + s[n + i]),(s[n - i] + " ")
        print(''.join(s))
        s = list((''.join(s)))
        k += 1
        e -= 1


    