from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        return sorted(counts.keys(), key=lambda word: (-counts[word], word))[:k]
