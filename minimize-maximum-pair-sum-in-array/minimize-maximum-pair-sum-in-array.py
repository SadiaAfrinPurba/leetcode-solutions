class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        front = 0
        rear = len(nums) - 1
        
        nums.sort()
        paired_sum = []
        
        while front < rear:
            running_sum = nums[front] + nums[rear]
            paired_sum.append(running_sum)
            
            front+=1
            rear-=1
        
        return max(paired_sum)
            