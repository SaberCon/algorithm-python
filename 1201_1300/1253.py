from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        ans = [[0] * len(colsum), [0] * len(colsum)]
        for i, col in enumerate(colsum):
            if col == 2:
                if upper == 0 or lower == 0:
                    return []
                ans[0][i] = 1
                ans[1][i] = 1
                upper -= 1
                lower -= 1
        for i, col in enumerate(colsum):
            if col == 1:
                if upper > 0:
                    ans[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][i] = 1
                    lower -= 1
                else:
                    return []
        if upper or lower:
            return []
        return ans
