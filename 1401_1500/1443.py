from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        connections = [[] for _ in range(n)]
        for f, t in edges:
            connections[f].append(t)
            connections[t].append(f)

        def dfs(node: int, father: int) -> int:
            ans = sum(dfs(child, node) for child in connections[node] if child != father)
            return ans + 2 if ans or hasApple[node] else 0

        return max(dfs(0, -1) - 2, 0)
