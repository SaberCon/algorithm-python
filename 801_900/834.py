class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        connections = [set() for _ in range(N)]
        for i, j in edges:
            connections[i].add(j)
            connections[j].add(i)

        counts = [0] * N

        def build_count(n, f):
            connections[n].discard(f)
            counts[n] = 1 + sum(build_count(c, n) for c in connections[n])
            return counts[n]

        build_count(0, 0)

        def get_distance(n):
            return sum(get_distance(c) + counts[c] for c in connections[n])

        ans = [get_distance(0)] + [0] * (N - 1)
        stack = [(c, 0) for c in connections[0]]
        while stack:
            n, father = stack.pop()
            ans[n] = ans[father] + N - 2 * counts[n]
            stack.extend((c, n) for c in connections[n])
        return ans
