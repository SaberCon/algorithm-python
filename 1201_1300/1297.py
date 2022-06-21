from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = Counter()
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                counter[sub] += 1
        return counter.most_common(1)[0][1] if len(counter) > 0 else 0
