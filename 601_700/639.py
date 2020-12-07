class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        last_2 = 1
        last_1 = 9 if s[-1] == '*' else (0 if s[-1] == '0' else 1)
        for c1, c2 in zip(reversed(s[:-1]), reversed(s)):
            if c1 == '0':
                curr = 0
            else:
                curr = 9 * last_1 if c1 == '*' else last_1
                if c1 == '1' or c1 == '*':
                    curr += last_2 * 9 if c2 == '*' else last_2
                if (c1 == '2' or c1 == '*') and c2 not in ('7', '8', '9'):
                    curr += last_2 * 6 if c2 == '*' else last_2
            last_1, last_2 = curr % mod, last_1 % mod
        return last_1
