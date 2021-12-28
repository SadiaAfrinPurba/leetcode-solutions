class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        #goal
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            num = nums.pop(0)
            
            permutations = self.permute(nums=nums)
            
            for permutation in permutations:
                permutation.append(num)
            
            ans.extend(permutations)
            nums.append(num)
        
        return ans
                
        
        