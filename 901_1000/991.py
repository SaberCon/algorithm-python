class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        mul = 0
        while startValue < target:
            startValue *= 2
            mul += 1
        delta = startValue - target
        return mul + delta // (2 ** mul) + sum(1 for d in bin(delta % (2 ** mul))[2:] if d == '1')
