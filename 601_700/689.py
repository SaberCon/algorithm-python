class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        length = len(nums) + 1 - k
        sums = [0] * length
        sums[0] = sum(nums[0:k])
        for i in range(length - 1):
            sums[i + 1] = sums[i] - nums[i] + nums[i + k]
        left_dp, right_dp = [], []
        for i in range(length):
            if not left_dp or left_dp[-1][1] < sums[i]:
                left_dp.append((i, sums[i]))
            else:
                left_dp.append(left_dp[-1])
        for i in range(length - 1, -1, -1):
            if not right_dp or right_dp[-1][1] <= sums[i]:
                right_dp.append((i, sums[i]))
            else:
                right_dp.append(right_dp[-1])
        max_sum = 0
        ans = []
        for i in range(k, length - k):
            curr = sums[i] + left_dp[i - k][1] + right_dp[length - i - k - 1][1]
            if curr > max_sum:
                max_sum = curr
                ans = [left_dp[i - k][0], i, right_dp[length - i - k - 1][0]]
        return ans
