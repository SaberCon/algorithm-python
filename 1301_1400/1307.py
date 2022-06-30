from collections import defaultdict
from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        count = defaultdict(lambda: 0)
        for i, c in enumerate(result):
            count[c] += 10 ** (len(result) - i - 1)
        for word in words:
            for i, c in enumerate(word):
                count[c] -= 10 ** (len(word) - i - 1)
        count = count.values()