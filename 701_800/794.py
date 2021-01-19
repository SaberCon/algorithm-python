class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        diagonals = [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
        columns = [''.join(col) for col in zip(*board)]
        win_x = board.count('XXX') + diagonals.count('XXX') + columns.count('XXX')
        win_o = board.count('OOO') + diagonals.count('OOO') + columns.count('OOO')
        count_x = sum(row.count('X') for row in board)
        count_o = sum(row.count('O') for row in board)
        if win_x == 0 and win_o == 0:
            return count_x == count_o or count_x - count_o == 1
        if win_x > 0 and win_o == 0:
            return count_x - count_o == 1
        if win_o > 0 and win_x == 0:
            return count_x == count_o
        return False
