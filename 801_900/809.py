class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def toCounts(s: str):
            ans = []
            for c in s:
                if ans and c == ans[-1][0]:
                    ans[-1][1] += 1
                else:
                    ans.append([c, 1])
            return ans

        S = toCounts(S)
        words = map(toCounts, words)
        return sum(len(word) == len(S) and all(c1[0] == c2[0] and (
            c1[1] >= c2[1] if c1[1] >= 3 else c1[1] == c2[1]) for c1, c2 in zip(S, word)) for word in words)
