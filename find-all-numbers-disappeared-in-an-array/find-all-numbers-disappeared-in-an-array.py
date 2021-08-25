class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mapper = dict()
        
        for num in nums:
            mapper[num] = 1
            
        result = list()
        
        for num in range(1, len(nums)+ 1):
            if num not in mapper:
                result.append(num)
        return result