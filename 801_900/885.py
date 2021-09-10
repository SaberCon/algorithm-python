class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [(rStart, cStart)]
        r, c = rStart, cStart + 1
        while len(ans) < rows * cols:
            if 0 <= r < rows and 0 <= c < cols:
                ans.append((r, c))
            if c > cStart and cStart - c < r - rStart < c - cStart:
                r += 1
            elif r > rStart and rStart - r < c - cStart <= r - rStart:
                c -= 1
            elif c < cStart and c - cStart < r - rStart <= cStart - c:
                r -= 1
            else:
                c += 1
        return ans
