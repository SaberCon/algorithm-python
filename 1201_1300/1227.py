class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp = 1
        for i in range(2, n):
            dp = (1 - 1 / (i * i)) * dp
        return 1 - (1 - 1 / n) * dp
