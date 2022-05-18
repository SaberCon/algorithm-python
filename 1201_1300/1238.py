from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [0]
        for i in range(n):
            ans.extend(j + 2 ** i for j in ans[::-1])
        p = ans.index(start)
        ans = ans[p:] + ans[:p]
        return ans
