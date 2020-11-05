class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        return ''.join(k * v for k, v in sorted(counts.items(), key=lambda i: -i[1]))
