class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            complement_mapper = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in complement_mapper:
                    return [i, complement_mapper[complement]]
                complement_mapper[nums[i]] = i