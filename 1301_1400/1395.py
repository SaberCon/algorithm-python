from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for i, r in enumerate(rating):
            l_less, r_less = sum(rating[j] < r for j in range(i)), sum(rating[j] < r for j in range(i + 1, n))
            l_more, r_more = i - l_less, n - 1 - i - r_less
            ans += l_less * r_more + r_less * l_more
        return ans
