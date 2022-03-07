class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        count = [(i, c) for i, c in enumerate(count) if c > 0]
        size = sum(c for _, c in count)
        mi, ma = count[0][0], count[-1][0]
        mean = sum(i * c for i, c in count) / size
        mode = max(count, key=lambda t: t[1])[0]
        seen = 0
        for j, (i, c) in enumerate(count):
            seen += c
            if seen >= size // 2 + 1:
                median = i if size % 2 or seen - c < size // 2 else (i + count[j - 1][0]) / 2
                break
        return [mi, ma, mean, median, mode]
