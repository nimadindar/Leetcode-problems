"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

# My solution with no algorithmic value

class Solution(object):
    def isAnagram(self, s, t):
        
        s = sorted(s)
        t = sorted(t)


        if s == t:
            return True
        return False
      
 # Algorithmic valueble solution

class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
  
        hashmapS , hashmapT = {}, {}
  
        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i],0) + 1
            hashmapT[t[i]] = hashmapT.get(t[i],0) + 1
    
        for c in hashmapS:
            if hashmapS[c] != hashmapT.get(c,0):
                return False
        return True
  
