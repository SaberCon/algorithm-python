from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        index, sum_1, sum_2 = -1, 0, 0
        for row in grid:
            new_index, new_sum_1, new_sum_2 = -1, 100000000, 100000000
            for i, n in enumerate(row):
                min_sum = n + (sum_1 if i != index else sum_2)
                if min_sum < new_sum_1:
                    new_index, new_sum_1, new_sum_2 = i, min_sum, new_sum_1
                elif min_sum < new_sum_2:
                    new_sum_2 = min_sum
            index, sum_1, sum_2 = new_index, new_sum_1, new_sum_2
        return sum_1
