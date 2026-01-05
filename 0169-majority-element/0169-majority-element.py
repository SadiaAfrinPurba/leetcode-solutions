from collections import Counter
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        maj = math.floor(n / 2)
        
        for key, val in count.items():
            if val > maj:
                return key