from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices > 4 * cheeseSlices or tomatoSlices < 2 * cheeseSlices or (tomatoSlices - 2 * cheeseSlices) % 2:
            return []
        total_jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        return [total_jumbo, cheeseSlices - total_jumbo]
