from collections import Counter
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        count_row = Counter(i for i, _ in indices)
        count_col = Counter(j for _, j in indices)
        return sum((count_row[i] + count_col[j]) % 2 for i in range(m) for j in range(n))
