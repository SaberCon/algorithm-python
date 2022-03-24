from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_edges = [[] for _ in range(n)]
        for a, b in redEdges:
            red_edges[a].append(b)
        blue_edges = [[] for _ in range(n)]
        for a, b in blueEdges:
            blue_edges[a].append(b)
        ans = [-1] * n
        ans[0] = 0
        queue = deque(((True, 0, 0), (False, 0, 0)))
        seen = {(True, 0), (False, 0)}
        count = 0
        while queue:
            color, index, length = queue.popleft()
            for next_index in (red_edges if color else blue_edges)[index]:
                next_color = not color
                if (next_color, next_index) in seen:
                    continue
                seen.add((next_color, next_index))
                queue.append((next_color, next_index, length + 1))
                ans[next_index] = length + 1 if ans[next_index] < 0 else min(ans[next_index], length + 1)
            if count == n:
                break
        return ans
