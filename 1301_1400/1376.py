from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                subordinates[m].append(i)

        def dfs(employee: int) -> int:
            return informTime[employee] + max((dfs(s) for s in subordinates[employee]), default=0)

        return dfs(headID)
