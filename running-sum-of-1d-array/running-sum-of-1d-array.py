class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = list()
        if not nums:
            return result 
        
        result.append(nums[0])
        if len(nums) == 1:
            return result
        
        for idx in range(1, len(nums)):
            running_sum = nums[idx] + result[idx - 1]
            result.append(running_sum)
        return result
            