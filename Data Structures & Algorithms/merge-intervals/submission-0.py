from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals

        intervals.sort()

        # print(intervals)

        result = [intervals[0]]
       

        for i in range(1, len(intervals)):

            if result[-1][0] <= intervals[i][0] <= result[-1][1] or result[-1][0] <= intervals[i][1] <= result[-1][1]:
                result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]
            else:
                result += [intervals[i]]

        return result







