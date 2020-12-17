class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = [i for i in range(len(edges) + 1)]

        def find_root(n):
            while uf[n] != n:
                n = uf[n]
            return n

        for n1, n2 in edges:
            r1, r2 = find_root(n1), find_root(n2)
            if r1 == r2:
                return [n1, n2]
            uf[r2] = r1
