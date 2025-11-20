class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda i: (i[1], i[0]))
        p1, p2 = -1, -1

        for start, end in intervals:
            if start > p2:
                res += 2
                p1, p2 = end - 1, end
            
            elif start > p1:
                res += 1

                if p2 == end:
                    p1 = end - 1
                else:
                    p1, p2 = p2, end
        return res
        