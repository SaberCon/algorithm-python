class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = {(0, 0)}
        for p in path:
            if p == 'E':
                x += 1
            if p == 'W':
                x -= 1
            if p == 'N':
                y += 1
            if p == 'S':
                y -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
