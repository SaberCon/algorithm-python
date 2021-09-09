from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        visited = Counter()
        for word in (s1 + ' ' + s2).split():
            visited[word] += 1
        return [k for k, v in visited.items() if v == 1]
