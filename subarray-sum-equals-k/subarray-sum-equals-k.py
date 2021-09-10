class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        total_subarray = 0
        subarray_sum = 0
        
        for num in nums:
            subarray_sum += num
            
            if subarray_sum-k in seen:
                total_subarray += seen[subarray_sum - k]
            
            if subarray_sum not in seen:
                seen[subarray_sum] = 1
            else:
                seen[subarray_sum] += 1
        return total_subarray

            
                
            
        