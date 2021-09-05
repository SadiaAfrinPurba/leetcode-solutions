class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = [0, 0]
        start_idx = 0
        end_idx = 0
        if 1 not in nums:
            return 0 
        for i, num in enumerate(nums):
            if num == 1:
                end_idx = i
            else:
                start_idx = i + 1
                
            if longest[1] - longest[0] < end_idx - start_idx:
                longest = [start_idx, end_idx]
                
        max_consecutive_ones = nums[longest[0]: longest[1] + 1]
        
        return len(max_consecutive_ones)
        