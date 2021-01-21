class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        last_min_swap = [0, 1]
        for i in range(1, len(A)):
            min_swap = [1000, 1000]
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                min_swap[0] = min(min_swap[0], last_min_swap[0])
                min_swap[1] = min(min_swap[1], last_min_swap[1] + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                min_swap[0] = min(min_swap[0], last_min_swap[1])
                min_swap[1] = min(min_swap[1], last_min_swap[0] + 1)
            last_min_swap = min_swap
        return min(last_min_swap)
