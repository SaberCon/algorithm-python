from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        counts = [0] * 10
        for d in digits:
            counts[d] += 1
        r = sum(i * c for i, c in enumerate(counts)) % 3
        if r:
            for i in range(r, 9, 3):
                if counts[i] >= 1:
                    counts[i] -= 1
                    break
            else:
                n = 2
                for i in range(3 - r, 9, 3):
                    m = min(counts[i], n)
                    counts[i] -= m
                    n -= m
                    if n == 0:
                        break
        if counts[0] > 0 and all(counts[i] == 0 for i in range(1, 10)):
            return '0'
        return ''.join(str(i) * c for i, c in reversed(list(enumerate(counts))))
