from collections import Counter


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = Counter()
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i, diff] = dp[j, diff] + 1
        return max(dp.values()) + 1
