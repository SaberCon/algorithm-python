from collections import Counter


class Solution:
    def minSwapsCouples(self, row: [int]) -> int:
        row = [[row[i] // 2, row[i + 1] // 2] for i in range(0, len(row), 2)]
        uf = [i for i in range(len(row))]

        def find_root(i):
            while uf[i] != i:
                i = uf[i]
            return i

        for l, r in row:
            l_r, r_r = find_root(l), find_root(r)
            uf[l_r] = r_r
        return sum(c - 1 for c in Counter(find_root(i) for i in uf).values())
