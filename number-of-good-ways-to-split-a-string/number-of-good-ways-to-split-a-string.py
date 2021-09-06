class Solution:
    def numSplits(self, s: str) -> int:
        if not s:
            return 0
        
        prefix = [0] * len(s)
        
        unique = set()
        
        for i in range(len(s)):
            unique.add(s[i])
            prefix[i] = len(unique)
            
        unique.clear()
        total = 0
        
        for j in range(len(s) - 1, 0, -1):
            unique.add(s[j])
            
            if prefix[j - 1] == len(unique):
                total += 1
        return total
        