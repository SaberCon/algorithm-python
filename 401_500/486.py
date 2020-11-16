class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[len(nums) - 1] >= 0
