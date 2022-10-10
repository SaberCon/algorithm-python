import math
from typing import List


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def get_center(p1, p2):
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            d = math.sqrt(r ** 2 - math.dist(p1, (mx, my)) ** 2)
            a = math.atan2(float(p1[1] - p2[1]), float(p1[0] - p2[0]))
            return mx + d * math.sin(a), my - d * math.cos(a)

        n = len(darts)
        ans = 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if math.dist(darts[i], darts[j]) > 2 * r:
                    continue
                center = get_center(darts[i], darts[j])
                ans = max(ans, sum(math.dist(dart, center) <= r + 1e-8 for dart in darts))
        return ans
