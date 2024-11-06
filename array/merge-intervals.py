class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            lastEnd = merged[-1][1]
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if currStart > lastEnd:
                merged.append([currStart, currEnd])
            else:
                merged[-1][1] = max(lastEnd, currEnd)
        return merged

        
        