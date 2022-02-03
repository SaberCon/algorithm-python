class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        ma = c - a - 2
        mi = 0 if ma == 0 else (1 if b - a < 3 or c - b < 3 else 2)
        return [mi, ma]
