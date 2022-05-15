import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [(0, 0)]
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            p += dp[bisect.bisect_right(dp, (s, 10 ** 9)) - 1][1]
            if p > dp[-1][1]:
                dp.append((e, p))
        return dp[-1][1]
