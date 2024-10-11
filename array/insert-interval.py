class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # start is sorted by ascending order
        # insert newInterview st sorted by start and no overlapping intervals
        # return intervals
        res = []
        for i in range(len(intervals)):
            # non overlap 1: new's end is before curr's start
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # non overlap 2: new's start is after curr's end
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # merge overlap 3
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

        