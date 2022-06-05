from itertools import combinations
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        for player, turn in (('A', 0), ('B', 1)):
            for (x1, y1), (x2, y2), (x3, y3) in combinations((m for i, m in enumerate(moves) if i % 2 == turn), 3):
                if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                    return player
        return 'Draw' if len(moves) == 9 else 'Pending'
