from itertools import chain


def diff(x1, y1, x2, y2, x3, y3):
    if x1 == x3:
        return 0
    return y1 + (x2 - x1) * ((y3 - y1) / (x3 - x1)) - y2


class Solution:
    def outerTrees(self, points: [[int]]) -> [[int]]:
        top, bottom = [], []
        points.sort()
        for point in points:
            top.append(point)
            bottom.append(point)
            while len(top) > 2 and diff(*top[-3], *top[-2], *top[-1]) > 0:
                del top[-2]
            while len(bottom) > 2 and diff(*bottom[-3], *bottom[-2], *bottom[-1]) < 0:
                del bottom[-2]
        return [[x, y] for (x, y) in
                {(x, y) for (x, y) in chain(top, bottom, (p for p in points if p[0] == points[-1][0]))}]
