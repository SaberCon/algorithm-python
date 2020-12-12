class Solution:
    def strangePrinter(self, s: str) -> int:
        chars = []
        for c in s:
            if chars and chars[-1] == c:
                continue
            chars.append(c)

        cache = {}

        def count(l, r):
            if l >= r:
                return 0
            if (l, r) in cache:
                return cache[l, r]
            cache[l, r] = count(l + 1, r) + 1
            for i in range(l + 1, r):
                if chars[i] != chars[l]:
                    continue
                cache[l, r] = min(cache[l, r], count(l, i) + count(i + 1, r))
            return cache[l, r]

        return count(0, len(chars))
