from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = - 1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], n = n, max(arr[i], n)
        return arr
