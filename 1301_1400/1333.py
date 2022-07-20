from typing import List


class Solution:
    def filterRestaurants(self, rs: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
            List[int]:
        rs = ((r, i) for i, r, v, p, d in rs if v >= veganFriendly and p <= maxPrice and d <= maxDistance)
        return [i for r, i in sorted(rs, reverse=True)]
