from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        freq = defaultdict(int)
        ans = []
        
        def key(val):
            return (freq[val], val)

        top = SortedList(key=key)
        rest = SortedList(key=key)
        current_sum = 0

        def rebalance():
            nonlocal current_sum
            while len(top) < min(x, len(freq)) and rest:
                best = rest.pop(-1)
                top.add(best)
                current_sum += freq[best] * best
            while len(top) > x:
                worst = top.pop(0)
                current_sum -= freq[worst] * worst
                rest.add(worst)
            while top and rest:
                worstTop = top[0]
                bestRest = rest[-1]
                if (freq[bestRest] > freq[worstTop] or
                   (freq[bestRest] == freq[worstTop] and bestRest > worstTop)):
                    top.remove(worstTop)
                    rest.remove(bestRest)
                    top.add(bestRest)
                    rest.add(worstTop)
                    current_sum += freq[bestRest] * bestRest - freq[worstTop] * worstTop
                else:
                    break

        for i, v in enumerate(nums):
            if freq[v] > 0:
                if v in top:
                    top.remove(v)
                    current_sum -= freq[v] * v
                else:
                    rest.remove(v)
            freq[v] += 1
            rest.add(v)
            rebalance()

            if i >= k:
                u = nums[i - k]
                if u in top:
                    top.remove(u)
                    current_sum -= freq[u] * u
                else:
                    rest.remove(u)
                if freq[u] == 1:
                    del freq[u]
                else:
                    freq[u] -= 1
                    rest.add(u)
                rebalance()

            if i >= k - 1:
                ans.append(current_sum)

        return ans