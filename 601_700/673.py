class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1, 1)] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    if dp[i][0] == dp[j][0] + 1:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
                    if dp[i][0] <= dp[j][0]:
                        dp[i] = (dp[j][0] + 1, dp[j][1])
        top = max(l for l, _ in dp)
        return sum(c for l, c in dp if l == top)
