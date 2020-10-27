class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, index) for index, (start, end) in enumerate(intervals))
        ends = sorted((end, index) for index, (start, end) in enumerate(intervals))

        ans = [-1] * len(intervals)
        curr = 0
        for end, index in ends:
            while starts[curr][0] < end:
                curr += 1
                if curr >= len(intervals):
                    return ans
            ans[index] = starts[curr][1]
        return ans
