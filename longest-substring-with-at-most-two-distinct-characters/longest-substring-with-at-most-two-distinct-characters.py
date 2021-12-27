class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_mapper = {}
        max_sub_str = 0
        start = 0
        
        for end, ch in enumerate(s):
            if len(char_mapper) < 2 and ch not in char_mapper:
                char_mapper[ch] = True
                window_size = (end - start) + 1
                max_sub_str = max(max_sub_str, window_size)
                
            elif ch in char_mapper:
                window_size = (end - start) + 1
                max_sub_str = max(max_sub_str, window_size)
                
            else:
                char_mapper = {}
                char_mapper[s[end - 1]] = True
                char_mapper[ch] = True
                start = end - 1
                
                while s[start] == s[start - 1]:
                    start -= 1
                
                window_size = (end - start) + 1
                max_sub_str = max(max_sub_str, window_size)
                
                
        return max_sub_str
                
                
                
            
        