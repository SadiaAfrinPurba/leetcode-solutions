class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        res = []
        perms = []
        
        def backtrack():
            if len(perms) == len(nums):
                res.append(perms[:])
                return
            
            for n in counter:
                if counter[n] > 0:
                    perms.append(n)
                    counter[n] -= 1
                    
                    backtrack()
                    
                    counter[n] += 1
                    perms.pop()
                    
        backtrack()
        
        return res
                    

        
        
            
            
        