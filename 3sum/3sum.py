class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = list()
        
        for idx in range(len(nums)-2):
            current = nums[idx]
            low = idx + 1
            high = len(nums) -1
            
            while low < high:
                current_sum = current + nums[low] + nums[high]
                if current_sum > 0:
                    high -= 1
                elif current_sum < 0:
                    low += 1
                else:
                    if [current, nums[low], nums[high]] not in result:
                        result.append([current, nums[low], nums[high]])
                    high -= 1
                    low += 1
                    
        return result
                        
                    
        