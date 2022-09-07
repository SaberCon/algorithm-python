from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(v % 2 for v in Counter(s).values()) <= k if len(s) >= k else False
