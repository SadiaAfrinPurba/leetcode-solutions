class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start_idx = 0
        longest = [0, 0]
        
        for i, char in enumerate(s):
            if char in seen:
                start_idx = max(start_idx, seen[char] + 1)
            
            if longest[1] - longest[0] < i - start_idx:
                longest = [start_idx, i]
                
            seen[char] = i
                
        max_substring = s[longest[0]:longest[1] + 1]
        
        return len(max_substring)
        