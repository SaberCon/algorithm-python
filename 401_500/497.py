from random import randint


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        total = 0
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += area
            self.areas.append(total)

    def pick(self) -> List[int]:
        point = randint(1, self.areas[-1])
        left, right = 0, len(self.areas) - 1
        while left < right:
            mid = (left + right) // 2
            if self.areas[mid] >= point:
                right = mid
            else:
                left = mid + 1
        index = self.areas[left] - point
        x1, y1, x2, y2 = self.rects[left]
        return x1 + index % (x2 - x1 + 1), y1 + index // (x2 - x1 + 1)
