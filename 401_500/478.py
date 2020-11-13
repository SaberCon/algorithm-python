import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            ran_x = random.uniform(self.x - self.r, self.x + self.r)
            ran_y = random.uniform(self.y - self.r, self.y + self.r)
            if ((ran_x - self.x) ** 2 + (ran_y - self.y) ** 2) <= self.r ** 2:
                break
        return ran_x, ran_y
