class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        ans = []
        
        for _ in range(len(nums)):
            num = nums.pop(0)
            perms = self.permuteUnique(nums)
            
            for perm in perms:
                perm.append(num)
                
                if perm not in ans:
                    ans.extend([perm])
            nums.append(num)
        
        return ans
        
        
            
            
        