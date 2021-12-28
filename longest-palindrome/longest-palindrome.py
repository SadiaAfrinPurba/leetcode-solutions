class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        ans = 0
        odd = 0
        for count in counter.values():
            if count > 1:
                if count % 2 == 0:
                    ans += count
                else:
                    ans += count - 1
                    odd += 1
            else:
                odd += 1
                
        if odd > 0:
            ans += 1
            
        return ans
            
                
            
        
        
         