class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        is_arithmetic = [True for _ in range(length)]
        ans = 0
        for i in range(2, length):
            last_ans = ans
            for j in range(0, length - i):
                if is_arithmetic[j] and A[j + 1] - A[j] == A[j + i] - A[j + i - 1]:
                    ans += 1
                else:
                    is_arithmetic[j] = False
            if last_ans == ans:
                break
        return ans
