class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(k, n):
            if n == 0:
                return 0
            if k == 1:
                return n
            if (k, n) in memo:
                return memo[k, n]
            l, r = 1, (n + 1) // 2
            while l < r - 1:
                mid = (l + r) // 2
                if dp(k - 1, mid - 1) > dp(k, n - mid):
                    r = mid
                else:
                    l = mid
            memo[k, n] = min(max(dp(k - 1, l - 1), dp(k, n - l)), max(dp(k - 1, r - 1), dp(k, n - r))) + 1
            return memo[k, n]

        return dp(k, n)
