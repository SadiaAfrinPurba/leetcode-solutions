class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = dict()
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                return True
        return False
        