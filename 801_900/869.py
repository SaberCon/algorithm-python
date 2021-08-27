class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        for i in range(32):
            target = str(2 ** i)
            if len(target) < len(digits):
                continue
            if len(target) > len(digits):
                break
            if sorted(target) == digits:
                return True
        return False
