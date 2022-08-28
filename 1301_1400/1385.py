from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        m, n = len(arr1), len(arr2)
        i = j = ans = 0
        while i < m and j < n:
            if arr1[i] < arr2[j] - d:
                i += 1
                ans += 1
            elif arr1[i] > arr2[j] + d:
                j += 1
            else:
                i += 1
        ans += m - i
        return ans
