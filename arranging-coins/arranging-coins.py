class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        for i in range(1, n+1):
            triangular_num = (i * (i + 1)) // 2
            
            if n < triangular_num:
                return i-1
            elif n == triangular_num:
                return i
        