# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:42:05 2021

@author: PURUBOI
"""

"""
I/P-1 : purushotham
O/P-1 : r

I/P-1 : testing
O/P-1 : s

I/P-1 : testings
O/P-1 : i

"""

def nonRepeatedSecondElement(s):
    d=dict()
    for i in range(len(s)):
        a=s[i]
        c=0
        for j in range(len(s)):
            if a==s[j]:
                c+=1
        d[s[i]]=c
    l=[]
    for k in d.keys():
        if d[k]==1:
            l.append(k)
    print(l[1])
    
s='testings'
c=nonRepeatedSecondElement(s)
print(s+" : "+c)
print("*"*40)

s='purushotham'
c=nonRepeatedSecondElement(s)
print(s+" : "+c)
print("*"*40)

s='testings'
c=nonRepeatedSecondElement(s)
print(s+" : "+c)
print("*"*40)