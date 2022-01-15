class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        last = values[0] - 1
        for v in values[1:]:
            ans = max(ans, v + last)
            last = max(last, v)
            last -= 1
        return ans
