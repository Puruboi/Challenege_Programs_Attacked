# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:38:59 2021

@author: PURUBOI
"""
"""
I/P-1 : [8,4,1,2,5,6,6,4,7,6,9]
O/P-1 : [4, 4, 6, 6, 6, 8, 1, 2, 5, 7, 9]

I/P-1 : [8,4,1,2,5,6,6,8,4,7,6,9]
O/P-1 : [8, 8, 4, 4, 6, 6, 6, 1, 2, 5, 7, 9]

I/P-1 : [6,8,4,1,2,5,6,6,8,4,7,6,9]
O/P-1 : [6, 6, 6, 6, 8, 8, 4, 4, 1, 2, 5, 7, 9]



"""
def dupsFirst(ar):
    a=dict()
    l1=[]
    l2=[]
    for i in range(len(ar)):
        ch=ar[i]  # taking each element 
        c=0
        for j in range(len(ar)):
            if ch==ar[j]:
                c+=1
        a[ch]=c
    for k in a.keys():
        if a[k]>1:
            l1+=[k]*(a[k])
        else:
            l2+=[k]*(a[k])
            
    return l1,l2


ar = [8,4,1,2,5,6,6,4,7,6,9]
l1,l2=dupsFirst(ar)
print(ar)
print(l1+l2)
print("*"*40)

ar = [8,4,1,2,5,6,6,8,4,7,6,9]
l1,l2=dupsFirst(ar)
print(ar)
print(l1+l2)
print("*"*40)

ar = [6,8,4,1,2,5,6,6,8,4,7,6,9]
l1,l2=dupsFirst(ar)
print(ar)
print(l1+l2)
print("*"*40)







            
    