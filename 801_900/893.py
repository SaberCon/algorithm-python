from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def find_special(word):
            return (tuple(sorted(Counter(w for i, w in enumerate(word) if i % 2).items())),
                    tuple(sorted(Counter(w for i, w in enumerate(word) if not i % 2).items())))

        return len({find_special(word) for word in words})
