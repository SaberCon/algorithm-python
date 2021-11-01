class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        point_set = set((x, y) for x, y in points)
        ans = 10 ** 10
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if 0 < (x2 - x1) * (y2 - y1) < ans and (x1, y2) in point_set and (x2, y1) in point_set:
                    ans = (x2 - x1) * (y2 - y1)
        return ans if ans < 10 ** 10 else 0
