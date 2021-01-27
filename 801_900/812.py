from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5 * abs(x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3)
                   for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))
