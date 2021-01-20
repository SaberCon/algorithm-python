class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        memo = {}

        def find_path(source):
            if source in memo:
                return memo[source]
            memo[source] = []
            for nex in graph[source]:
                if nex == target:
                    memo[source].append([source, target])
                for path in find_path(nex):
                    memo[source].append([source] + path)
            return memo[source]

        return find_path(0)
