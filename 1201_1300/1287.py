from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        min_size = len(arr) // 4 + 1
        for i in range(len(arr) - min_size + 1):
            if arr[i] == arr[i + min_size - 1]:
                return arr[i]
