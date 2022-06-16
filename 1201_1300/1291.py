from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for size in range(len(str(low)), len(str(high)) + 1):
            for i in range(1, 10 - size + 1):
                num = sum((i + j) * (10 ** (size - j - 1)) for j in range(size))
                if num < low:
                    continue
                if num > high:
                    break
                ans.append(num)
        return ans
