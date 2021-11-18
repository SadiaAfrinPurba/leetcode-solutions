class Solution:
           def findDuplicates(self, nums: List[int]) -> List[int]:
            ans = set()

            for num in nums:
                if nums[abs(num) - 1] < 0:
                    ans.add(abs(num))
                else:
                    nums[abs(num) - 1] = nums[abs(num) - 1] * -1

            return list(ans)
        