class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}

        def find_root(node):
            if node not in uf or uf[node] == node:
                return node
            return find_root(uf[node])

        for x, y in stones:
            y = -y - 1
            x_root = find_root(x)
            y_root = find_root(y)
            uf[x] = uf[y] = uf[y_root] = x_root

        return len(stones) - len(set(find_root(n) for n in uf.values()))
