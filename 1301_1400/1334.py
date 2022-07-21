from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        a = [[distanceThreshold + 1] * n for _ in range(n)]
        for f, t, d in edges:
            a[f][t] = d
            a[t][f] = d
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    a[i][j] = min(a[i][j], a[i][k] + a[k][j])
        return min(range(n), key=lambda i: (sum(a[i][j] <= distanceThreshold and i != j for j in range(n)), -i))
