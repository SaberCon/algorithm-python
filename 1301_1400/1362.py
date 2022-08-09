from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int((num + 2) ** 0.5), 0, -1):
            for n in (num + 1, num + 2):
                if n % i == 0:
                    return [i, n // i]
        raise AssertionError()
