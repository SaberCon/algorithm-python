class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                continue
            if score > 0 and tokens[right] > tokens[left]:
                power += tokens[right] - tokens[left]
                left += 1
                right -= 1
                continue
            break
        return score
