class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = {}
        for num in nums:
            if frequency_count.get(num) is None:
                frequency_count[num] = 1
            else:
                frequency_count[num] += 1
        res = []
        for i in range(k):
            res.append(max(frequency_count, key=frequency_count.get))
            frequency_count.pop(res[i])
        
        return res
                
        