from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjvex = defaultdict(list)
        for x, y in connections:
            adjvex[x].append(y)
            adjvex[y].append(x)

        low = [0] * n  # dfs中通过无向边可以向前回溯到的最早的时间点
        T = 1
        res = []

        def tarjan(x: int, parent: int) -> None:
            nonlocal T
            low[x] = t = T
            T += 1

            for y in adjvex[x]:
                if y == parent:
                    continue
                if not low[y]:
                    tarjan(y, x)  # 先访问y, 访问了才能计算
                    if low[y] > t:  # x和y不在一个强连通分量
                        res.append([x, y])
                low[x] = min(low[x], low[y])

        tarjan(0, -1)
        return res
