class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res =0
        k = 3
        for n in nums:
            remain = n % k
            res += min(remain, k -remain)
        return res