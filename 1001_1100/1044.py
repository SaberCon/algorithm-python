class Solution:
    def longestDupSubstring(self, s: str) -> str:
        a1, a2 = 26, 27
        mod = 2 ** 31 - 1
        n = len(s)
        arr = [ord(c) - ord('a') for c in s]

        def check(length):
            aL1, aL2 = pow(a1, length, mod), pow(a2, length, mod)
            h1, h2 = 0, 0
            for i in range(length):
                h1 = (h1 * a1 + arr[i]) % mod
                h2 = (h2 * a2 + arr[i]) % mod
            seen = {(h1, h2)}
            for start in range(1, n - length + 1):
                h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + length - 1]) % mod
                h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + length - 1]) % mod
                if (h1, h2) in seen:
                    return start
                seen.add((h1, h2))
            return -1

        l, r = 0, n - 1
        start = -1
        while l < r:
            m = (l + r + 1) // 2
            idx = check(m)
            if idx != -1:
                l = m
                start = idx
            else:
                r = m - 1
        return s[start:start + l]
