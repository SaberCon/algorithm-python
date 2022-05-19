from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = {0}
        for a in arr:
            if len(set(a)) == len(a):
                mask = sum(1 << (ord(c) - ord('a')) for c in a)
                masks |= {m | mask for m in masks if m & mask == 0}
        return max(bin(s).count('1') for s in masks)
