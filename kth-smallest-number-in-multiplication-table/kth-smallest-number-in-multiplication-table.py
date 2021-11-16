import itertools
import numpy as np

class Solution:
    def count(self, m: int, target: int, n: int):
        return sum(min(target // row, n) for row in range(1, m+1))
    
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        low, high, ans = 1, m * n, 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.count(m, mid, n) < k:
                low = mid + 1
            
            else:
                high = mid - 1
                ans = mid
                
        return ans

            

        
                
        