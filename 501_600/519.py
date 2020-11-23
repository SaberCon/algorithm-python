from random import randint


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.visited = set()
        self.rows = n_rows
        self.cols = n_cols

    def flip(self) -> List[int]:
        while True:
            rand = randint(0, self.rows * self.cols - 1)
            x, y = rand // self.cols, rand % self.cols
            if (x, y) not in self.visited:
                self.visited.add((x, y))
                return [x, y]

    def reset(self) -> None:
        self.visited.clear()
