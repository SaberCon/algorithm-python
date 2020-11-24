class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        height, width = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

        def reveal_empty(x, y):
            if x < 0 or x >= height or y < 0 or y >= width or board[x][y] != 'E':
                return
            mines = 0
            for dx, dy in directions:
                if 0 <= x + dx < height and 0 <= y + dy < width and board[x + dx][y + dy] == 'M':
                    mines += 1
            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    reveal_empty(x + dx, y + dy)

        reveal_empty(click[0], click[1])
        return board
