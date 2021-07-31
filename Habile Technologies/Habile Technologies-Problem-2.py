# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:16:27 2021

@author: PURUBOI
"""

"""
Problem 2:
----------
Expand a given string with "spaces" and "swaps" 

   - Step 1: Expand with "spaces" from the center towards the start/end of the string in each step.
       i) string with no middle character adds a middle single space
              e.g. ""BATA" " becomes "BA TA" and becomes “B A T A”
       ii) string with middle character adds left and right space. A space is introduced before and after a 'character' or a 'substring'.
              e.g. ""BATIA" " becomes "BA T IA" and becomes "B A T I A"
   - Step 2: Once space is added in each step then it is followed by character swap (swap between character after left space and character before right space). Swap happens and continues between all the opposite characters till the center (space or middle character) of the string is reached.
       e.g.   
       "BA TA" becomes "BA TA"     (swap for middle space will be same)
       "B A T A" becomes "B T A A" (swap between A and T, followed by continuous swap till the middle empty space)

       e.g. 
       "BA T IA" becomes "BA T IA" (swap middle character T will be in the same position)
       "B A T I A" becomes “B I T A A” (swap between A and I, followed by continuous swap till the middle character ‘T’)

   - Step 3: Print the output
   - Step 4: Iterate from Step 1

All the intermediate outputs should be printed as below.

Example 1:
Input: 
       BATA
Output: 
       BA TA     # addition of space in middle, followed by swap in middle space
       B T A A   # addition of space (before A and after T) followed by swap of 'T' and 'A' followed by a swap for middle space.


Example 2:

Input: 
       BATIA
Output: 
       BA T IA     
       B I T A A 

Example 3:

Input: 
       CAPITOL
Outputs:
       CAP I TOL       # addition of space(before and after I) swaps 'I' which has no change since it is at the center
       CA T I P OL     # addition of space(before T and after P) swaps 'P' and 'T'. Followed by a swap of 'I.
       C O P I T A L   # addition of space(before A and after O) swaps 'A' and 'O'. Followed by a swap of 'T' and 'P'.  Followed by a swap of 'I'. (swap till the middle is reached)

Example 4:
Input: 
       CARDBOARD 
Output:
       CARD B OARD
       CAR O B D ARD
       CA A D B O R RD
       C R R O B D A A D

Example 5:
Input: 
       BATAMA
Output:
       BAT AMA
       BA A T MA
       B M T A A A

"""

def withMiddleEle(s):
    from math import floor
    
    s = list(s)
    n = floor(len(s)/2)
    
    i=0
    d ,k ,e = n ,1 ,(n-1)
    
    # BASE CASE
    
    s[n - i],s[n + i] = (s[n + i]),(s[n - i])
    s[n - i],s[n + i] = (" " + s[n + i] + " "),(" " + s[n - i] + " ")
    print(''.join(s))
    s = list((''.join(s)))
    
    # Iterative Adding space and Swaping
    
    while k<d:
        i = 0
        n = floor(len(s)/2)
        c = n - e
        while i < c:
            s[n - i],s[n + i] = (s[n + i]),(s[n - i])
            i += 1
        s[n - i],s[n + i] = (" " + s[n + i]),(s[n - i] + " ")
        print(''.join(s))
        s = list((''.join(s)))
        k += 1
        e -= 1

def withoutMiddleEle(s):
    from math import floor
    
    s = list(s)
    n = floor(len(s)/2)
    d = n - 1
    k = 1
    e = d
    s.insert(n," ")
    print(''.join(s))
    s = list((''.join(s)))
    while k <= d:
        i = 0
        n = floor(len(s)/2)
        while i < n-e:
            s[n - i],s[n + i] = (s[n + i]),(s[n - i])
            i +=1
        s[n - i],s[n + i] = (" " + s[n + i]),(s[n - i] + " ")
        print(''.join(s))
        s = list((''.join(s)))
        k +=1
        e -=1
        
def main(s):
    a=len(s)
    if a%2==0:
        withoutMiddleEle(s)
    else:
        withMiddleEle(s)
        
print("Example-1")        
main('BATA')
print('-'*30)

print("Example-2")
main('BATIA')
print('-'*30)

print("Example-3")
main('CAPITOL')
print('-'*30)

print("Example-4")
main('CARDBOARD')
print('-'*30)

print("Example-5")
main('BATAMA')

