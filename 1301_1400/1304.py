from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 2:
            return [1, -1]
        return [i for i in range(n - 1)] + [-(n - 1) * (n - 2) // 2]
