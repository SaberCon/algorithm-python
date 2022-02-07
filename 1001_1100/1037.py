class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (x1 - x2) * (y1 - y3) != (x1 - x3) * (y1 - y2)
