from functools import cache


class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def dp(left, right):
            if left >= right:
                return 0
            if s[left] == s[right]:
                return dp(left + 1, right - 1)
            return min(dp(left + 1, right), dp(left, right - 1)) + 1

        return dp(0, len(s) - 1)
