class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A) - 1):
            if A[i] == i:
                continue
            if A[i] == i + 1 and A[i + 1] == i:
                A[i], A[i + 1] = i, i + 1
                continue
            return False
        return True
