from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = {(i, j) for i, j in queens}
        ans = []
        ki, kj = king
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                for t in range(1, 8):
                    i, j = ki + di * t, kj + dj * t
                    if not (0 <= i < 8 and 0 <= j < 8):
                        break
                    if (i, j) in queens:
                        ans.append([i, j])
                        break
        return ans
