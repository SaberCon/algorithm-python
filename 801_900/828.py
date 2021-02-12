class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mod = 10 ** 9 + 7
        last = ans = 0
        letters = {c: (-1, -1) for c in s}
        for i, c in enumerate(s):
            p1, p2 = letters[c]
            letters[c] = (p2, i)
            last += i - p2 - p2 + p1
            ans += last
            ans %= mod
        return ans
