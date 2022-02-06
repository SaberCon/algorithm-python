from collections import deque


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        last, x_len = -1, 0
        xs = {}
        for x in sorted({x for x, _ in blocked} | {source[0], target[0], 0, 999999}):
            if x > last + 1:
                x_len += 1
            xs[x] = x_len
            last = x
            x_len += 1

        last, y_len = -1, 0
        ys = {}
        for y in sorted({y for _, y in blocked} | {source[1], target[1], 0, 999999}):
            if y > last + 1:
                y_len += 1
            ys[y] = y_len
            last = y
            y_len += 1
        source, target = (xs[source[0]], ys[source[1]]), (xs[target[0]], ys[target[1]])
        seen = {(xs[x], ys[y]) for x, y in blocked}
        seen.add(source)

        queue = deque((source,))
        while queue:
            x, y = queue.popleft()
            if (x, y) == target:
                return True
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < x_len and 0 <= ny < y_len and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny))
        return False
