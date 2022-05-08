from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        rules = {'a': ('e',), 'e': ('a', 'i'), 'i': ('a', 'e', 'o', 'u'), 'o': ('i', 'u'), 'u': ('a',)}

        @cache
        def dp(size, prev):
            if size == 0:
                return 1
            return sum(dp(size - 1, c) for c in rules[prev]) % MOD

        return sum(dp(n - 1, c) for c in ('a', 'e', 'i', 'o', 'u')) % MOD
