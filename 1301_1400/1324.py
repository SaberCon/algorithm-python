from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        return [''.join(w[i] if len(w) > i else ' ' for w in words).rstrip() for i in range(max(len(w) for w in words))]
