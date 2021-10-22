class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        sum_1 = arr.count(1)
        if sum_1 == 0:
            return [0, 2]
        if sum_1 % 3:
            return [-1, -1]
        starts = []
        count_1 = 0
        for i, n in enumerate(arr):
            if n == 1:
                if count_1 % (sum_1 // 3) == 0:
                    starts.append(i)
                count_1 += 1
        size = len(arr) - starts[-1]
        for i in range(size):
            if arr[starts[0] + i] != arr[starts[1] + i] or arr[starts[0] + i] != arr[starts[2] + i]:
                return [-1, -1]
        return [starts[0] + size - 1, starts[1] + size]
