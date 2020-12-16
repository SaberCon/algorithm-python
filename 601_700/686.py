class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        s = a * max(2, ((2 * len(b) + len(a) - 1) // len(a)))
        try:
            m = s.index(b) + len(b)
        except ValueError:
            return -1
        return (m + len(a) - 1) // len(a)
