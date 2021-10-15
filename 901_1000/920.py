from functools import cache


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(n, n - k, -1):
            ans = (ans * i) % MOD

        @cache
        def count_lists(remained, unplayed):
            if remained == 0:
                return 1
            if remained == unplayed:
                ans = 1
                for i in range(1, remained + 1, 1):
                    ans = (ans * i) % MOD
                return ans
            return ((n - k - unplayed) * count_lists(remained - 1, unplayed)
                    + unplayed * count_lists(remained - 1, unplayed - 1)) % MOD

        return ans * count_lists(goal - k, n - k) % MOD
