from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.arr = list(range(size))

    def find(self, i: int) -> int:
        if self.arr[i] != i:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def unite(self, i1: int, i2: int) -> bool:
        i1, i2 = self.find(i1), self.find(i2)
        if i1 == i2:
            return False
        self.arr[i1] = i2
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted((w, a, b, i) for i, (a, b, w) in enumerate(edges))
        uf = UnionFind(n)
        value = sum(w for w, a, b, i in edges if uf.unite(a, b))

        ans = [[], []]
        for w, a, b, i in edges:
            uf = UnionFind(n)
            uf.unite(a, b)
            v = w + sum(w for w, a, b, i in edges if uf.unite(a, b))
            if v > value:
                continue

            uf = UnionFind(n)
            if sum(w for w, a, b, _i in edges if _i != i and uf.unite(a, b)) > value \
                    or any(uf.find(i) != uf.find(0) for i in range(n)):
                ans[0].append(i)
            else:
                ans[1].append(i)

        return ans
