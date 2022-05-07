from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(p % 2 for p in position), sum(1 - p % 2 for p in position))
