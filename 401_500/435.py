class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: (i[1], i[0]))
        count = 0
        last = intervals[0][0]
        for start, end in intervals:
            if start < last:
                continue
            count += 1
            last = end
        return len(intervals) - count
