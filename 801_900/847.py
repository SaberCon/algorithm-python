class Solution:
    def shortestPathLength(self, graph: [[int]]) -> int:
        if len(graph) < 2:
            return 0
        seen = set()
        queue = [((i, 1 << i), 0) for i in range(len(graph))]
        while True:
            (cur, cover), count = queue.pop(0)
            for nex in graph[cur]:
                new_cover = cover | (1 << nex)
                if new_cover == (1 << len(graph)) - 1:
                    return count + 1
                start_cover = (nex, new_cover)
                if start_cover in seen:
                    continue
                seen.add(start_cover)
                queue.append((start_cover, count + 1))
