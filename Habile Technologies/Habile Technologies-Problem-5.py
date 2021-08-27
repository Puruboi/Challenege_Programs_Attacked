# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:38:09 2021

@author: PURUBOI
"""
# Triplets Program

ar=[3,1,4,6,5]

def func1(ar):
    for i in range(len(ar)):
        a=ar[0]
        for j in range(i+1,len(ar)):
            b=ar[1]
            c=(a*b)+(b*b)
            for k in range(j+1,len(ar)):
                d=(ar[k]**2)
                if c==d:
                    return True
    else:
        return False

func1(ar)
        













