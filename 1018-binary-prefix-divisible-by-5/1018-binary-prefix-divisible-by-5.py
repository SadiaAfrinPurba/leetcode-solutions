class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = 0
        for n in nums:
            curr = (curr << 1) + n # left shift, similar to multiplying to 2
            res.append(curr % 5 == 0)
        return res
        
        