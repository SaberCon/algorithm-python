from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def count_word(word):
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            return arr

        letters = count_word(letters)
        dp = [([0] * 26, 0)]
        for word in words:
            s = sum(score[ord(c) - ord('a')] for c in word)
            a = count_word(word)
            for i in range(len(dp)):
                na = [c1 + c2 for c1, c2 in zip(a, dp[i][0])]
                if all(c1 <= c2 for c1, c2 in zip(na, letters)):
                    dp.append((na, s + dp[i][1]))
        return max(s for _, s in dp)
