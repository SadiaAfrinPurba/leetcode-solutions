class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:

            # the res dict will have (1,2,0,,0, meaning 0th idx is representing a, 25th idx is representing z)
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            # python does not allow list to be the key value
            res[tuple(count)].append(s)
 
        return list(res.values())