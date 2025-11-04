from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answers = []
        for i in range(len(nums)-k+1):
            count = Counter(nums[i:i+k])

            if len(count) <= x:
                answers.append(sum(nums[i:i+k]))
            else:
                pair = list(count.items())
                pair.sort(key=lambda p: (p[1], p[0]), reverse=True)

                curr_sum = 0
                for num, c in pair[:x]:
                    curr_sum += num * c
                answers.append(curr_sum)    
        return answers
        