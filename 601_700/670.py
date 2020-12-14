class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        sorted_s = ''.join(sorted(str(num), reverse=True))
        for i, (c, sorted_c) in enumerate(zip(s, sorted_s)):
            if c == sorted_c:
                continue
            idx = s.rindex(sorted_c)
            return int(s[:i] + sorted_c + s[i + 1:idx] + c + s[idx + 1:])
        return int(s)
