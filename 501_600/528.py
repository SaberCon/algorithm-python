from random import randint


class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        for weight in w:
            self.w.append(weight + (self.w[-1] if self.w else 0))

    def pickIndex(self) -> int:
        rand = randint(0, self.w[-1] - 1)
        left, right = 0, len(self.w) - 1
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] > rand:
                right = mid
            else:
                left = mid + 1
        return left
