class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        valid_idx = list(range(len(nums)))
        longest = 0
        
        for arr_idx, num in enumerate(nums):
            current = arr_idx
            ans = set()
            while nums[current] in valid_idx:
                ans.add(nums[current])
                current = nums[current]
                valid_idx.remove(current)
            
            longest = max(longest, len(ans))
        return longest
        
        