import heapq
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        target = box = player = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    target = (i, j)
                if grid[i][j] == 'B':
                    box = (i, j)
                if grid[i][j] == 'S':
                    player = (i, j)
                if grid[i][j] != '#':
                    grid[i][j] = '.'
        seen = {(box, player)}
        heap = [(0, box, player)]
        while heap:
            pushes, box, player = heapq.heappop(heap)
            px, py = player
            for next_player in ((px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)):
                npx, npy = next_player
                if 0 <= npx < m and 0 <= npy < n and grid[npx][npy] == '.':
                    if box != next_player and (box, next_player) not in seen:
                        heapq.heappush(heap, (pushes, box, next_player))
                        seen.add((box, next_player))
                    elif box == next_player:
                        next_box = nbx, nby = px + (npx - px) * 2, py + (npy - py) * 2
                        if 0 <= nbx < m and 0 <= nby < n and grid[nbx][nby] == '.':
                            if next_box == target:
                                return pushes + 1
                            if (next_box, next_player) not in seen:
                                heapq.heappush(heap, (pushes + 1, next_box, next_player))
                                seen.add((next_box, next_player))
        return -1
