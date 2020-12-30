class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 10 ** 9 + 7
        cache = {}

        def count_palindromic(l, r):
            if (l, r) in cache:
                return cache[l, r]
            cache[l, r] = 0
            for c in ('a', 'b', 'c', 'd'):
                try:
                    li = S.index(c, l, r)
                    ri = S.rindex(c, l, r)
                    if li == ri:
                        cache[l, r] += 1
                    else:
                        cache[l, r] += 2 + count_palindromic(li + 1, ri)
                    cache[l, r] %= mod
                except ValueError:
                    continue
            return cache[l, r]

        return count_palindromic(0, len(S))
