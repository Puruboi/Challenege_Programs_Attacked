# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:25:15 2021

@author: PURUBOI
"""

a=[8,9,5,6,7,8,9,1,3,6,6,7]
c=[]
d=0
for i in a:
    if i not in c:
        d+=1
        c.append(i)
print(c,d)
    
    