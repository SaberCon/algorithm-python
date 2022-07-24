class Solution:
    def numberOfSteps(self, num: int) -> int:
        return sum(2 if b == '1' else 1 for b in bin(num)[2:]) - 1
