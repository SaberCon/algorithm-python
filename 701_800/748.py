class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = [c.lower() for c in licensePlate if c != ' ' and not c.isdigit()]
        words.sort(key=len)
        for word in words:
            remaining = letters.copy()
            for c in word:
                if c in remaining:
                    remaining.remove(c)
            if not remaining:
                return word
