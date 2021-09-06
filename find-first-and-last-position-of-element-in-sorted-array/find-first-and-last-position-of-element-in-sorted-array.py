class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos = -1
        last_pos = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            
            if target == nums[mid]:
                first_pos = mid 
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        if first_pos >= 0:
            for i in range(first_pos , len(nums)):
                if nums[i] == target:
                    last_pos = i
                    
        return [first_pos, last_pos]
        
        