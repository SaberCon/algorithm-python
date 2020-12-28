import bisect


class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j + 1] = [(left, right)]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_left(self.ranges, (left, float('inf'))) - 1
        return i >= 0 and right <= self.ranges[i][1]

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        if i > j:
            return
        merge = []
        if self.ranges[i][0] < left:
            merge.append((self.ranges[i][0], left))
        if self.ranges[j][1] > right:
            merge.append((right, self.ranges[j][1]))
        self.ranges[i:j + 1] = merge

    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.ranges) and self.ranges[i + d - 1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j - d + 1][0] > right:
                j -= d
        return i, j
