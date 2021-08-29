class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_number_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        
        return n_number_sum - actual_sum
        