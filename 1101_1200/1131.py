class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        def zip_arrays(i, j):
            return (n1 * i + n2 * j + n3 for n1, n2, n3 in zip(arr1, arr2, range(len(arr1))))

        return max(max(zip_arrays(i, j)) - min(zip_arrays(i, j)) for i in (1, -1) for j in (1, -1))
