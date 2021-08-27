# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 12:26:27 2021

@author: PURUBOI
"""
def checknum(s):
    for i in s:
        if '0'<=i<='9':
            return 1
        
def checkalpha(s):
    for i in s:
        if 'A'<=i<='Z':
            return 1
def checkspl(s):
    for i in s:
        if i in '!@#$%^&*_':
            return 1
def checkminlen(s,min):
    if len(s)>4:
        return 1
def checkspsl(s):
    if " \/+" not in s:
        return 1
def checkstart(s):
    if s[0] not in '0123456789':
        return 1

def passwordcheck(s):
    if (checknum(s) and checkalpha(s) and checkspl(s) and 
        checkminlen(s,4) and checkspsl(s) and checkstart(s)):
        return 1
    else:
        return 0
            
s='aaA123C'
s1="aCd34!4rf" 
s2="asd!2 /we"            
print(passwordcheck(s))
print(passwordcheck(s1))
print(passwordcheck(s2))