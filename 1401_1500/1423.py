from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = ans = sum(cardPoints[:k])
        for i in range(k):
            score += cardPoints[-(i + 1)] - cardPoints[k - i - 1]
            ans = max(ans, score)
        return ans
