class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(1, int(c ** 0.5) + 1):
            if int((c - i ** 2) ** 0.5) ** 2 == c - i ** 2:
                return True
        return False
