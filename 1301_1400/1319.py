from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        computers = [[] for _ in range(n)]
        for a, b in connections:
            computers[a].append(b)
            computers[b].append(a)
        seen = set()

        def dfs(i: int):
            seen.add(i)
            for j in computers[i]:
                if j not in seen:
                    dfs(j)

        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans - 1
