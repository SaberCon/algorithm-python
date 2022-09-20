from functools import cache


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 1
            if s[i] == '0':
                return 0
            ans = 0
            for j in range(i + 1, n + 1):
                if int(s[i:j]) > k:
                    break
                ans += dp(j)
            return ans % 1000000007

        return dp(0)
