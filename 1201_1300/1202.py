from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        uf = [i for i in range(N)]

        def find(i):
            n = uf[i]
            if n != i:
                n = find(n)
                uf[i] = n
            return n

        def union(i1, i2):
            n1, n2 = find(i1), find(i2)
            uf[n1] = n2

        for i, j in pairs:
            union(i, j)

        uf_map = defaultdict(list)
        for i in range(N):
            uf_map[find(i)].append(s[i])
        for k in uf_map:
            uf_map[k] = sorted(uf_map[k], reverse=True)

        return ''.join(uf_map[find(i)].pop() for i in range(N))
