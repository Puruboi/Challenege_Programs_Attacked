# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:19:35 2021

@author: PURUBOI
"""
# Find Mininum Squares Sum equals to N

def func1(n):
    c=0
    a=int(n**0.5)
    if a*a==n:
        c+=1
        return c
    
    if (a*a)<n:
        temp=n
        while temp:
            c+=1
            temp=temp-(a*a)
            a=int(temp**0.5)
        return c

n1=24
n2=6
n3=10
n4=36
print(func1(n1))
print(func1(n2))
print(func1(n3))
print(func1(n4))