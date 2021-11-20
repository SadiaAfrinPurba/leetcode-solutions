class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0
        
        
        if high == 0:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[high] != nums[high - 1]:
            return nums[high]
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 != 0 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
            
        
        