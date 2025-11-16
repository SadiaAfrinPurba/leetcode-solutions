class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        new_start, new_end = newInterval

        for current in intervals:
            end = current[1]
            if end >= new_start:
                break
            else:
                res.append(current)
                i += 1
        
        res.append(newInterval)
        
        for j in range(i, len(intervals)):
            previous = res[-1]
            current_start, current_end = intervals[j][0], intervals[j][1]
            previous_start, previous_end = previous[0], previous[1]

            if previous_end >= current_start:
                start = min(previous_start, current_start)
                end = max(previous_end, current_end)
                res[-1] = [start, end]
            
            else:
                res.append(intervals[j])
        
        return res


        