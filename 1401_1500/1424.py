from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i, row in enumerate(nums):
            for j, n in enumerate(row):
                ans.append((i + j, j, n))
        return [n for _, _, n in sorted(ans)]
