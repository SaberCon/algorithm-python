class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dp = {}

        def calc_point(l, r, k):
            if l > r:
                return 0
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            if (l, r, k) in dp:
                return dp[l, r, k]
            points = calc_point(l, r - 1, 1) + k * k
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    points = max(points, calc_point(l, i, k + 1) + calc_point(i + 1, r - 1, 1))
            dp[l, r, k] = points
            return points

        return calc_point(0, len(boxes) - 1, 1)
