from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = 0
        ans = 0
        for l, r in sorted(intervals, key=lambda i: (i[0], -i[1])):
            if r > covered:
                ans += 1
                covered = r
        return ans
