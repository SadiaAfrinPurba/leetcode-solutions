class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        count = 0
        for i in range(len(s)):
            if s[i] == t[i]:
                count += 1
        
        return count == len(s) 
            