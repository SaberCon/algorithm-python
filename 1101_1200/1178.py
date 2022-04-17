from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def to_mask(word):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            return mask

        counts = Counter(mask for mask in map(to_mask, words) if bin(mask).count('1') <= 7)

        def to_masks(puzzle):
            puzzle = [1 << (ord(c) - ord('a')) for c in puzzle]
            for i in range(1 << 6):
                mask = puzzle[0]
                for j in range(6):
                    if i & (1 << j):
                        mask |= puzzle[j + 1]
                yield mask

        return [sum(counts[mask] for mask in to_masks(puzzle)) for puzzle in puzzles]
