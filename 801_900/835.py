from collections import Counter


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        points1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        points2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        if not points1 or not points2:
            return 0
        deltas = Counter()
        for i1, j1 in points1:
            for i2, j2 in points2:
                deltas[i1 - i2, j1 - j2] += 1
        return deltas.most_common(1)[0][1]
