from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = {}
        t_counter = {}
        
        for char in s:
            if s_counter.get(char) == None:
                s_counter[char] = 1
            else:
                s_counter[char] += 1
                
        for char in t:
            if t_counter.get(char) == None:
                t_counter[char] = 1
            else:
                t_counter[char] += 1
        
        return s_counter == t_counter
        
        
        
      
            