class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        uf = [i for i in range(len(edges) + 1)]

        def find_root(n):
            while uf[n] != n:
                n = uf[n]
            return n

        invalid = first_invalid = second_invalid = None
        children = set()
        for f, c in edges:
            if c in children:
                invalid = c
                break
            children.add(c)

        for i, (f, c) in enumerate(edges):
            if c == invalid:
                if not first_invalid:
                    first_invalid = (f, c)
                else:
                    second_invalid = (f, c)
                continue
            rf, rc = find_root(f), find_root(c)
            if rf == rc:
                return f, c
            uf[rc] = rf
        if find_root(first_invalid[0]) == find_root(first_invalid[1]):
            return first_invalid
        return second_invalid
