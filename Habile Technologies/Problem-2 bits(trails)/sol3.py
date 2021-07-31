# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:09:41 2021

@author: PURUBOI
"""

s=input()
a=len(s)
if a%2==0:
    from math import floor
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

if a%2!=0:
    from math import floor
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