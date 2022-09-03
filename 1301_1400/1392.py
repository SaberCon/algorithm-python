class Solution:
    def longestPrefix(self, s: str) -> str:
        base, mod, mul = 31, 10 ** 9 + 7, 1
        prefix = suffix = 0
        ans = 0
        for i in range(len(s) - 1):
            prefix = (prefix + mul * (ord(s[i]) - ord('a'))) % mod
            suffix = (suffix * base + ord(s[-i - 1]) - ord('a')) % mod
            mul = mul * base % mod
            if prefix == suffix:
                ans = i + 1
        return s[:ans]
