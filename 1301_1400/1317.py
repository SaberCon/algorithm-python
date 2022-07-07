from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = []
        carry = False
        for c in reversed(str(n)):
            d = int(c) - carry
            carry = d < 2
            if carry:
                d += 10
            ans.append(str(d // 2))
        if carry:
            ans.pop()
        ans = int(''.join(reversed(ans)))
        return [ans, n - ans]
