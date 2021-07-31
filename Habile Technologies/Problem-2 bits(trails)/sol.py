# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:11:18 2021

@author: PURUBOI
"""
from math import floor
s='CARDBOARD'
s=list(s)
n=floor(len(s)/2)
s[n-0],s[n+0]=(" "+s[n+0]+" "),(" "+s[n-0]+" ")
print(''.join(s))

s=list((''.join(s)))
n=floor(len(s)/2)
s[n-1],s[n+1]=(s[n+1]),(s[n-1])
s[n-2],s[n+2]=(" "+s[n+2]),(s[n-2]+" ")
print(''.join(s))

s=list((''.join(s)))
n=floor(len(s)/2)
s[n-2],s[n+2]=(s[n+2]),(s[n-2])
s[n-3],s[n+3]=(s[n+3]),(s[n-3])
s[n-4],s[n+4]=(" "+s[n+4]),(s[n-4]+" ")
print(''.join(s))

s=list((''.join(s)))
n=floor(len(s)/2)
s[n-2],s[n+2]=(s[n+2]),(s[n-2])
s[n-3],s[n+3]=(s[n+3]),(s[n-3])
s[n-4],s[n+4]=(s[n+4]),(s[n-4])
s[n-5],s[n+5]=(s[n+5]),(s[n-5])
s[n-6],s[n+6]=(" "+s[n+6]),(s[n-6]+" ")
print(''.join(s))
    

