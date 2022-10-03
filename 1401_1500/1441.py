from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        last = 1
        for t in target:
            ans.extend(["Push"] * (t - last))
            ans.extend(["Pop"] * (t - last))
            ans.append("Push")
            last = t + 1
        return ans
