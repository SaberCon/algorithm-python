from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(lambda: 0)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())
