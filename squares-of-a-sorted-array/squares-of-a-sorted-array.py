class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        low = 0
        high = n - 1
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            if abs(nums[low]) < abs(nums[high]):
                num = nums[high]
                high -= 1
            
            else:
                num = nums[low]
                low += 1
            
            ans[i] = num * num
            
        return ans
            