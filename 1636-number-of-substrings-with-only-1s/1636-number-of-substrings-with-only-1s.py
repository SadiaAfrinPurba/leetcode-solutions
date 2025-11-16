class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7

        res = 0
        consecutive = 0

        for ch in s:
            if ch == "1":
                consecutive += 1
                res += consecutive
            else:
                consecutive = 0
        
        return res % MOD

        