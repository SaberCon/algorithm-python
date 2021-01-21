class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        status = [0] * len(graph)

        def dfs(i):
            if status[i] == 1:
                return True
            if status[i] == -1:
                return False
            status[i] = -1
            for nex in graph[i]:
                if not dfs(nex):
                    return False
            status[i] = 1
            return True

        for i, edges in enumerate(graph):
            dfs(i)

        return [i for i, state in enumerate(status) if state > 0]
