from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.tree = []
        self.nodes = {}
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        def dfs(node: int, level: int, leaves: int) -> int:
            if level >= len(self.tree):
                self.tree.append([])
            if children[node]:
                for child in children[node]:
                    leaves = dfs(child, level + 1, leaves)
            else:
                leaves += 1
            self.tree[level].append((node, leaves))
            self.nodes[node] = (level, leaves)
            return leaves

        dfs(0, 0, 0)

    def getKthAncestor(self, node: int, k: int) -> int:
        level, leaves = self.nodes[node]
        if level < k:
            return -1
        arr = self.tree[level - k]
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid][1] >= leaves:
                end = mid
            else:
                start = mid + 1
        return arr[start][0]
