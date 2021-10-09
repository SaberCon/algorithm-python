from collections import defaultdict, deque


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        def parents(mouse, cat, turn):
            if turn == MOUSE:
                for c in graph[cat]:
                    if c:
                        yield mouse, c, 3 - turn
            else:
                for m in graph[mouse]:
                    yield m, cat, 3 - turn

        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m, c, MOUSE] = len(graph[m])
                degree[m, c, CAT] = len(graph[c]) - (0 in graph[c])

        color = defaultdict(int)
        queue = deque()
        for i in range(N):
            for t in (MOUSE, CAT):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        while queue:
            mouse, cat, turn, winner = queue.popleft()
            for m, c, t in parents(mouse, cat, turn):
                if color[m, c, t]:
                    continue
                if t == winner:
                    color[m, c, t] = t
                    queue.append((m, c, t, t))
                else:
                    degree[m, c, t] -= 1
                    if not degree[m, c, t]:
                        color[m, c, t] = 3 - t
                        queue.append((m, c, t, 3 - t))
        return color[1, 2, 1]
