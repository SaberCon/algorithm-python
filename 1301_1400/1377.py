from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        connections = [[] for _ in range(n + 1)]
        for v1, v2 in edges:
            connections[v1].append(v2)
            connections[v2].append(v1)
        connections[1].append(0)

        def prob(vertex: int, parent: int, seconds: int) -> float:
            neighbors = connections[vertex]
            children_count = len(neighbors) - 1
            if seconds == 0 or children_count == 0:
                return 1 if vertex == target else 0
            return 1 / children_count * max(prob(v, vertex, seconds - 1) for v in neighbors if v != parent)

        return prob(1, 0, t)
