from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        size = len(arr)
        dp = [1] * size
        for n, i in sorted((n, i) for i, n in enumerate(arr)):
            for j in range(i + 1, min(size, i + d + 1)):
                if arr[j] >= n:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= n:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
