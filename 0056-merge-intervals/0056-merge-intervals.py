class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for current in intervals[1:]:
            last = res[-1]
            curr_start_time = current[0]
            prev_end_time = last[1]
            if prev_end_time >= curr_start_time:
                start = last[0]
                end = max(current[1], last[1])
                res[-1] = [start, end]
            else:
                res.append(current)
        
        return res
