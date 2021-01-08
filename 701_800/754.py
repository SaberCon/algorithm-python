class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = int((target * 2) ** 0.5)
        while True:
            total = i * (i + 1) // 2
            if total >= target and (total % 2) == (target % 2):
                return i
            i += 1
