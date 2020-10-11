class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        count = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count += 1
                ans += count
            else:
                count = 0
        return ans
