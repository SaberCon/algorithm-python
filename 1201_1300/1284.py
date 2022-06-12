from collections import deque
from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        size = m * n
        target = sum(sum(b << j for j, b in enumerate(row)) << (i * n) for i, row in enumerate(mat))
        seen = {0}
        queue = deque(((0, 0),))
        while queue:
            mask, step = queue.popleft()
            if mask == target:
                return step
            for i in range(size):
                next_mask = mask ^ (1 << i)
                if i - n >= 0:
                    next_mask ^= 1 << (i - n)
                if i + n < size:
                    next_mask ^= 1 << (i + n)
                if i % n:
                    next_mask ^= 1 << (i - 1)
                if (i + 1) % n:
                    next_mask ^= 1 << (i + 1)
                if next_mask not in seen:
                    seen.add(next_mask)
                    queue.append((next_mask, step + 1))
        return -1
