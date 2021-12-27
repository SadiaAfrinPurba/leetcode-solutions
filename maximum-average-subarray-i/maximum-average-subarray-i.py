class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        window_sum = 0
        max_avg = float('-inf')
        
        for end in range(len(nums)):
            window_sum += nums[end]
            
            if (end - start) + 1 == k:
                avg = window_sum / k
                max_avg = max(max_avg, avg)
                window_sum -= nums[start]
                start += 1
                
        return max_avg
        