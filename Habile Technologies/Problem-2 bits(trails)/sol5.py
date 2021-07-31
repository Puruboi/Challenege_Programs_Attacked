# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:03:50 2021

@author: PURUBOI
"""

from math import floor
s='BATA'
def withoutMiddleEle(s):
    s=list(s)
    n=floor(len(s)/2)
    d=n-1
    k=1
    e=d
    s.insert(n," ")
    print(''.join(s))
    s=list((''.join(s)))
    while k<=d:
        i=0
        n=floor(len(s)/2)
        while i<n-e:
            s[n-i],s[n+i]=(s[n+i]),(s[n-i])
            i+=1
        s[n-i],s[n+i]=(" "+s[n+i]),(s[n-i]+" ")
        print(''.join(s))
        s=list((''.join(s)))
        k+=1
        e-=1
withoutMiddleEle(s)
