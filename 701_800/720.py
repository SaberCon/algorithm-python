class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        words.sort(key=lambda w: (-len(w), w))
        for word in words:
            for i in range(1, len(word) + 1):
                if i == len(word):
                    return word
                if word[:i] not in word_set:
                    break
        return ''
