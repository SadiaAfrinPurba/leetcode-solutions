class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mapping = {}

        for num in nums:
            mapping[num] = 1
        
        current_ori = original
        
        while current_ori in mapping:
            current_ori = current_ori * 2
        
        return current_ori

        