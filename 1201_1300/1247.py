class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        p1 = sum(c1 == 'x' and c2 == 'y' for c1, c2 in zip(s1, s2))
        p2 = sum(c1 == 'y' and c2 == 'x' for c1, c2 in zip(s1, s2))
        return -1 if (p1 + p2) % 2 else (p1 + 1) // 2 + (p2 + 1) // 2
