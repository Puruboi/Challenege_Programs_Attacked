# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:27:25 2021

@author: PURUBOI
"""

"""

1) Arrange the words in alphabetical order based on only the "first" character (not the second character and further characters). 
2) If two words are starting with the same character then the same order of the words should be maintained from the original sentence. 
      
Constraints for this problem:
    Use char[] or Character[] array for the input and output. (e.g., avoid in-built java.lang.String or similar class to represent 'string', instead use char[] to solve the problem). 
    e.g., 
       Java: 
              char input[] = "The domestic dog is a domesticated form of wolf".toCharArray() 
       Python: 
              input = list('The domestic dog is a domesticated form of wolf')
       Javascript:
              input = Array.from('hello')

Example 1:
Input: 
       this is an impossible task
Output: 
       an is impossible this task

       Explanation:
       'a' is the lowest, followed by 'i' and 't' character.
       an - first word because of 'a'
       'is impossible' - 'is' comes before 'impossible' since 'is' appears in the orginial sentence before 'impossible'.
       'this task' - 'this' comes before 'task' since 'this' appears in the orginial sentence before 'task'.

Example 2:
Input: 
       the domestic dog is a domesticated form of wolf
Output:
       a domestic dog domesticated form is of the wolf

"""
       
# Split function to split the string default it splits with space.

def alphabeticalOrdering(string):
    
    string = string.lower()
    
    def splitRep(string,ch=" "):
        k = 0
        l = []
        for i in range(len(string)):
            if string[i] == ch:
                l.append(string[k:i])
                k = i+1
            if i == (len(string)-1):
                l.append(string[k:i+1])
        return l
    
    def indexRep(string,ch):
        for i in range(len(string)):
            if ch == string[i]:
                return i
            
    def sortting(a):
        n = len(a)
        for i in range(n):
            for j in range(0,n-i-1):
                if a[j][0] > a[j+1][0]:
                    a[j],a[j+1] = a[j+1],a[j]
                if a[j][0] == a[j+1][0]:
                    a1 = indexRep(a,a[j])
                    a2 = indexRep(a,a[j+1])
                    
                    if a1 > a2:
                        a[j],a[j+1] = a[j+1],a[j]
                    if a1 < a2:
                        a[j],a[j+1] = a[j],a[j+1]
                        
    a = splitRep(string)
    sortting(a)
    print("Input_string: ",string)
    r = ''
    for i in a:
        r += i + " "
    print("Output_string: ",r)
    
    
string1 = 'this is an impossible task'
string2 = 'the domestic dog is a domesticated form of wolf'

print("Example-1")
alphabeticalOrdering(string1)
print('-'*30)

print("Example-1")
alphabeticalOrdering(string2)
print('-'*30)

                    


