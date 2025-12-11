
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for idx in range(len(strs[0])):
            for s in strs:
                if idx == len(s) or s[idx] != strs[0][idx]:
                    return res
            res += strs[0][idx]
        
        return res
