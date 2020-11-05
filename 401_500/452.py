class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda p: p[1])
        last_shot = - (2 ** 32) - 1
        for start, end in points:
            if start <= last_shot:
                continue
            ans += 1
            last_shot = end
        return ans
