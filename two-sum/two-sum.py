class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_mapper = {}
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in complement_mapper:
                return [i, complement_mapper[compliment]]
            complement_mapper[nums[i]] = i 
            
                
        
        