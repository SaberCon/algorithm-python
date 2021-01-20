class Solution:
    def bestRotation(self, A: [int]) -> int:
        size = len(A)
        points = [0] * (size + 1)
        for i, num in enumerate(A):
            points[i + 1] += 1
            if i >= num:
                points[0] += 1
                points[i - num + 1] -= 1
            else:
                points[size + i - num + 1] -= 1
        most = curr = ans = 0
        for i, point in enumerate(points):
            curr += point
            if curr > most:
                most = curr
                ans = i
        return ans
