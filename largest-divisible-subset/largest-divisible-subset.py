class Solution:
    def get_subset(self, nums: List[int]) -> List[int]:

        max_length = 0
        lis = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and lis[i] <= lis[j]:
                    lis[i] = 1 + lis[j]
                    max_length = max(max_length, lis[i])

        if max_length == 0:
            return nums[0:1]

        subset = self.build_subset(max_length, lis, nums)

        return subset

    def build_subset(self, max_length: int, arr: List[int], nums: List[int]) -> List[int]:
        subset = []
        prev = -1

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == max_length and (prev % nums[i] == 0 or prev == -1):
                subset.append(nums[i])
                max_length -= 1
                prev = nums[i]

        return subset

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        nums.sort()

        subset = self.get_subset(nums)

        return subset