from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def sum_array(n: int) -> int:
            return sum(min(a, n) for a in arr)

        mi, ma = 0, max(arr)
        while mi < ma:
            mid = (mi + ma + 1) // 2
            if sum_array(mid) < target:
                mi = mid
            else:
                ma = mid - 1
        return mi + (abs(sum_array(mi + 1) - target) < abs(sum_array(mi) - target))
