from functools import cache


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)

        @cache
        def longest_chain(word: str):
            if word not in words:
                return 0
            return max(longest_chain(word[:i] + word[i + 1:]) for i in range(len(word))) + 1

        return max(longest_chain(word) for word in words)
