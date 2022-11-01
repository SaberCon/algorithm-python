from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = [0] * k
        for num in arr:
            r = num % k
            if remainders[(k - r) % k]:
                remainders[(k - r) % k] -= 1
            else:
                remainders[r] += 1
        return all(count == 0 for count in remainders)
