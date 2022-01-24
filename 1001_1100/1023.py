class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        N = len(pattern)
        pattern += '$'

        def match(query):
            i = 0
            for c in query:
                if c == pattern[i]:
                    i += 1
                elif c.isupper():
                    return False
            return i == N

        return [match(q) for q in queries]
