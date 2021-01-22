class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        size = len(A)
        if size == 1:
            return False
        avg = sum(A)
        A = [a * size - avg for a in A]

        left, right = set(), set()
        for i in range(size // 2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left:
            return True
        for i in range(size // 2, size):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right:
            return True
        left.remove(sum(A[i] for i in range(size // 2)))
        return any(-half in right for half in left)
