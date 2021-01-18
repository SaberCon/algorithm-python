class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return all((abs(x - target[0]) + abs(y - target[1])) > (abs(target[0]) + abs(target[1])) for x, y in ghosts)
