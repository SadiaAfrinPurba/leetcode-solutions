class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        res = []
        for num, count in counter.items():
            if count == 1:
                res.append(num)
        return res
            
        
        
#         if len(nums) == 2:
#             if nums[0] != nums[1]:
#                 return nums
#             else:
#                 return []
                
#         j = 0
#         i = 1
#         while len(nums) > 2:
#             current_num = nums[j]
            
#             if current_num != nums[i]:
#                 i += 1
                
#                 if i >= len(nums):
#                     j += 1
#                     i = j + 1
            
#             elif current_num == nums[i]:
#                 match_num = nums[i]
#                 nums.remove(current_num)
#                 nums.remove(match_num)
#                 i = 1
#                 j = 0
                
#         return nums

            
            
        