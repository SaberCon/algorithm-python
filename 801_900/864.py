from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '@'][0]
        keys = sum(grid[i][j].islower() for i in range(m) for j in range(n))
        visited = [[[] for _ in range(n)] for _ in range(m)]

        def get_key_bit(char):
            return 2 ** (ord(char) - (ord('a') if char.islower() else ord('A')))

        queue = deque()
        queue.append((0, start, 0))
        while queue:
            moves, (x, y), key_bit = queue.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '#':
                    continue
                c = grid[nx][ny]
                new_key_bit = key_bit
                if c.isupper() and new_key_bit | get_key_bit(c) > new_key_bit:
                    continue
                if c.islower():
                    new_key_bit |= get_key_bit(c)
                    if new_key_bit == 2 ** keys - 1:
                        return moves + 1
                for kb in visited[nx][ny]:
                    if kb | new_key_bit == kb:
                        break
                else:
                    visited[nx][ny] = [kb for kb in visited[nx][ny] if kb | key_bit != new_key_bit] + [new_key_bit]
                    queue.append((moves + 1, (nx, ny), new_key_bit))
        return -1
