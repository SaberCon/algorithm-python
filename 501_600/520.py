class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() if word[0].islower() else (word.isupper() or word[1:].islower())
