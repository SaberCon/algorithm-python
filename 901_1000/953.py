class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}
        return all(tuple(order[c] for c in w1) <= tuple(order[c] for c in w2) for w1, w2 in zip(words, words[1:]))
