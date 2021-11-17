class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(0, m)]
        
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] =  dp[i - 1][j] + dp[i][j - 1] 
            
        return dp[-1][-1]
       