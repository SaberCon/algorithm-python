class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        N = len(arr)
        zeros = 0

        for i, n in enumerate(arr):
            if n == 0:
                zeros += 1
            if i + zeros >= N - 1:
                break

        for j in range(i, -1, -1):
            if arr[j] == 0:
                if j + zeros < N:
                    arr[j + zeros] = arr[j]
                zeros -= 1
            arr[j + zeros] = arr[j]
