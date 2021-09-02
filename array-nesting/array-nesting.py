class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        valid_idx = list(range(len(nums)))
        longest = 0
        
        for arr_idx, num in enumerate(nums):
            current = arr_idx
            count = 0
            while nums[current] in valid_idx:
                current = nums[current]
                count += 1
                valid_idx.remove(current)
            longest = max(longest, count)
        return longest
        
        