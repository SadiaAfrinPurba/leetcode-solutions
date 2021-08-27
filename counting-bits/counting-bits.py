import collections

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            binary_repr = bin(i)
            bin_count = collections.Counter(binary_repr)
            ans.append(bin_count['1'])
            
        return ans
            
            
        