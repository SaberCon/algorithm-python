from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        queue = deque()
        j = 1
        ans = -10 ** 9
        for i, (x1, y1) in enumerate(points):
            while j < n and points[j][0] - x1 <= k:
                v = sum(points[j])
                while queue and queue[-1][1] <= v:
                    queue.pop()
                queue.append((j, v))
                j += 1
            if queue and queue[0][0] == i:
                queue.popleft()
            if queue:
                ans = max(ans, y1 - x1 + queue[0][1])
        return ans
