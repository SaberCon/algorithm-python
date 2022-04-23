class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        dp = max_sum = 0
        for _ in range(min(2, k)):
            for n in arr:
                dp = max(dp, 0) + n
                max_sum = max(max_sum, dp)
        if k == 1:
            return max_sum
        return (max(sum(arr), 0) * (k - 2) + max_sum) % 1000000007
