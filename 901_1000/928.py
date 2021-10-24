from collections import defaultdict, Counter


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        N = len(graph)
        initial.sort()
        connection = defaultdict(set)

        for i in range(N - 1):
            for j in range(i + 1, N):
                if graph[i][j] == 1:
                    connection[i].add(j)
                    connection[j].add(i)

        infected = [[] for _ in range(N)]
        for i in initial:
            visited = set(initial)
            queue = [i]
            while queue:
                cur = queue.pop()
                infected[cur].append(i)
                for nex in connection[cur]:
                    if nex not in visited:
                        queue.append(nex)
                        visited.add(nex)

        ans = initial[0]
        size = 0
        for i, count in sorted(Counter(nodes[0] for nodes in infected if len(nodes) == 1).items()):
            if count > size:
                ans = i
                size = count
        return ans
