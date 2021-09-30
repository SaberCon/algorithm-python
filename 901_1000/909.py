from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([(1, 0)])
        seen = {1}
        while queue:
            curr, count = queue.popleft()
            for i in range(curr + 1, min(curr + 6, n * n) + 1):
                v = board[n - 1 - ((i - 1) // n)][n - 1 - (i - 1) % n if ((i - 1) // n) % 2 else (i - 1) % n]
                next = i if v < 0 else v
                if next == n * n:
                    return count
                if next not in seen:
                    seen.add(next)
                    queue.append((next, count + 1))
        return -1
