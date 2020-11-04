class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            distances = {}
            for x2, y2 in points:
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                distances.setdefault(distance, 0)
                distances[distance] += 1
            for count in distances.values():
                ans += count * (count - 1)
        return ans
