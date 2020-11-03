class Solution:
    def numberOfArithmeticSlices(self, A: [int]) -> int:
        counts = [{} for _ in A]
        ans = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                distance = A[i] - A[j]
                counts[i].setdefault(distance, 0)
                counts[i][distance] += 1 + counts[j].get(distance, 0)
                ans += counts[j].get(distance, 0)
        return ans
