class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        
        prev = lower - 1
        
        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else upper + 1
            
            if prev + 1 <= current - 1:
                result.append(self.format_result(prev + 1, current - 1))
                
            prev = current
        return result
        
        
    def format_result(self, lower, upper):
        if lower == upper:
            return str(lower)
        else:
            return f'{str(lower)}->{str(upper)}'
        