class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {c: 0 for c in 'balloon'}
        for c in text:
            if c in counts:
                counts[c] += 1
        counts['l'] //= 2
        counts['o'] //= 2
        return min(counts.values())
