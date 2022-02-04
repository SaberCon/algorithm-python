class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        seen = set()

        def dfs(x, y, c):
            if (x, y) in seen:
                return True
            if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] != c:
                return False
            seen.add((x, y))
            next_squares = sum(dfs(nx, ny, c) for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
            if next_squares < 4:
                grid[x][y] = color
            return True

        dfs(row, col, grid[row][col])
        return grid
