class Solution:
    def robotSim(self, commands: [int], obstacles: [[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = 0
        pos = (0, 0)
        ans = 0
        for c in commands:
            if c == -2:
                direction = (direction - 1) % 4
            elif c == -1:
                direction = (direction + 1) % 4
            else:
                for _ in range(c):
                    next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
                    if next_pos in obstacles:
                        break
                    pos = next_pos
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans
