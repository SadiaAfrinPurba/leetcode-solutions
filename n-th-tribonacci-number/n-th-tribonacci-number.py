class Solution:
    def tribonacci(self, n: int, memo: dict = {}) -> int:
        
        if n in memo:
            return memo[n]
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 1
        
        value = self.tribonacci(n - 1, memo) +  self.tribonacci(n - 2, memo) + self.tribonacci(n - 3, memo)
        
        memo[n] = value
        
        return value