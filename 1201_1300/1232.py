from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        return all((x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2) for x3, y3 in coordinates[2:])
