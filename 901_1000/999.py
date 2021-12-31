class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ri, rj = next((i, j) for i in range(8) for j in range(8) if board[i][j] == 'R')
        ans = 0
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            i, j = ri + di, rj + dj
            while 0 < i < 8 and 0 < j < 8 and board[i][j] == '.':
                i += di
                j += dj
            if 0 < i < 8 and 0 < j < 8 and board[i][j] == 'p':
                ans += 1
        return ans
