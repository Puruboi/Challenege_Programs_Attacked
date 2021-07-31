# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:26:38 2021

@author: PURUBOI
"""
from math import floor
s='BATAMA'
s=list(s)
n=floor(len(s)/2)
s.insert(n," ")
print(''.join(s))

s=list((''.join(s)))
n=floor(len(s)/2)
#s[n-1],s[n+1]=(s[n+1]),(s[n-1])
s[n-1],s[n+1]=(" "+s[n+1]),(s[n-1]+" ")
print(''.join(s))

s=list((''.join(s)))
n=floor(len(s)/2)
s[n-1],s[n+1]=(s[n+1]),(s[n-1])
s[n-3],s[n+3]=(" "+s[n+3]),(s[n-3]+" ")
print(''.join(s))