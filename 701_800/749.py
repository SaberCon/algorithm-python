class Solution:
    def containVirus(self, grid: [[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def is_invalid(i, j):
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1

        def find_infections(i, j):
            if is_invalid(i, j) or grid[i][j] == 2 or (i, j) in infected:
                return 0
            if grid[i][j] == 0:
                infected.add((i, j))
                return 1
            grid[i][j] = 2
            return sum(find_infections(i + di, j + dj) for di, dj in directions)

        def build_walls(i, j):
            if is_invalid(i, j):
                return 0
            if grid[i][j] == 0:
                return 1
            grid[i][j] = -1
            return sum(build_walls(i + di, j + dj) for di, dj in directions)

        def spread(i, j):
            if is_invalid(i, j) or grid[i][j] == 1:
                return
            if grid[i][j] == 0:
                grid[i][j] = 1
                return
            grid[i][j] = 1
            for di, dj in directions:
                spread(i + di, j + dj)

        ans = 0
        while True:
            coord = (-1, -1)
            most_infections = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        infected = set()
                        infections = find_infections(i, j)
                        if infections > most_infections:
                            most_infections = infections
                            coord = (i, j)
            if most_infections == 0:
                return ans
            ans += build_walls(*coord)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        spread(i, j)