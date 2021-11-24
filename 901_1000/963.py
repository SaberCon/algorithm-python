from itertools import permutations


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = set(map(tuple, points))

        ans = float('inf')
        for (x1, y1), (x2, y2), (x3, y3) in permutations(points, 3):
            x4, y4 = x2 + x3 - x1, y2 + y3 - y1
            if (x4, y4) in points:
                v21 = complex(x2 - x1, y2 - y1)
                v31 = complex(x3 - x1, y3 - y1)
                if abs(v21.real * v31.real + v21.imag * v31.imag) < 1e-7:
                    ans = min(ans, abs(v21) * abs(v31))
        return ans if ans < float('inf') else 0
