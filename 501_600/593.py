class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        p1, p2, p3, p4 = sorted((p1, p2, p3, p4))
        return p1 != p2 and distance(p1, p2) == distance(p3, p4) == distance(p1, p3) == distance(p2, p4) \
               and distance(p1, p4) == distance(p2, p3)
