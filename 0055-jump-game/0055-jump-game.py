class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1 # last element

        # iterate in a reverse order, -1 is exclusive so, it will reach to 0
        for i in range(n - 1, -1, -1):
            max_jump = nums[i]

            if i + max_jump >= target:
                target = i

        return target == 0



        