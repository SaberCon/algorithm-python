from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -1, -1]
        for num in nums:
            new_dp = dp.copy()
            for i in range(3):
                if dp[i] < 0:
                    continue
                p = (num + i) % 3
                new_dp[p] = max(dp[p], dp[i] + num)
            dp = new_dp
        return dp[0]
