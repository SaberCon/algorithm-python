from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        return Counter(filter(lambda w: w not in banned, ''.join(
            l.lower() if l.isalpha() else ' ' for l in paragraph).split())).most_common(1)[0][0]
