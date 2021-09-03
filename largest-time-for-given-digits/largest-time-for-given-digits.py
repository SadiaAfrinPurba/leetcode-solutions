from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
              
        all_permutation = list(permutations(sorted(arr, reverse=True)))
        
        for h1, h2, m1, m2 in all_permutation:
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            
            if hour < 24 and minute < 60:
                return f'{h1}{h2}:{m1}{m2}'
        return ''
            
            
        