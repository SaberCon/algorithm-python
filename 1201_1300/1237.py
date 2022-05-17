from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x: int, y: int) -> int:
        pass


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x1, y1, x2, y2 = 1, 1, 1000, 1000
        while x1 <= x2 and y1 <= y2:
            a = customfunction.f(x1, y2)
            if a == z:
                ans.append([x1, y2])
            if a < z:
                x1 += 1
            else:
                y2 -= 1
        return ans
