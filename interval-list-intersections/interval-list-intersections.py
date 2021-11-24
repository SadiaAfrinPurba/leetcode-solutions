class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a_prt, b_prt = 0, 0
        ans = []
        
        while a_prt < len(firstList) and b_prt < len(secondList):
            s1, e1 = firstList[a_prt]
            s2, e2 = secondList[b_prt]
            
            if s1 <= e2 and s2 <= e1:
                ans.append([max(s1, s2), min(e1, e2)])
            
            if e1 < e2:
                a_prt += 1
            else:
                b_prt += 1
                
        return ans
                
            
        