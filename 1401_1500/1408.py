from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        return [w for i, w in enumerate(words) if any(w in words[j] for j in range(i + 1, len(words)))]
