from functools import cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        m = len(evil)
        fail = [0] * m

        @cache
        def get_trans(stats, ch):
            while stats > 0 and evil[stats] != ch:
                stats = fail[stats - 1]
            return stats + (evil[stats] == ch)

        for i in range(1, m):
            fail[i] = get_trans(fail[i - 1], evil[i])

        @cache
        def dp(pos, stats, bound):
            if stats == m:
                return 0
            if pos == n:
                return 1

            ans = 0
            l = (ord(s1[pos]) if bound & 1 else ord('a'))
            r = (ord(s2[pos]) if bound & 2 else ord('z'))
            for i in range(l, r + 1):
                ch = chr(i)
                next_stats = get_trans(stats, ch)
                next_bound = ((ch == s1[pos]) | ((ch == s2[pos]) << 1)) & bound
                ans += dp(pos + 1, next_stats, next_bound)
            return ans % 1000000007

        return dp(0, 0, 3)
