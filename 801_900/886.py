class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        uf = [i for i in range(n + 1)]

        def find_root(num):
            if uf[num] == num:
                return num
            root = find_root(uf[num]) if uf[num] > 0 else -find_root(-uf[num])
            uf[num] = root
            return root

        for n1, n2 in dislikes:
            r1 = find_root(n1)
            r2 = find_root(n2)
            if r1 == r2:
                return False
            if r2 > 0:
                uf[r2] = -r1
            else:
                uf[-r2] = r1
        return True
