class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, start):
            res.append(curr.copy()) # do not want to change the curr state

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(curr, i + 1)
                curr.pop()
        
        dfs([], 0)
        return res