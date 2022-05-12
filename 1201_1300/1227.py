class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp = 0
        for i in range(2, n):
            prob = 1 / (i * i)
            dp = prob + (1 - prob) * dp
        return 1 / n + (1 - 1 / n) * dp
