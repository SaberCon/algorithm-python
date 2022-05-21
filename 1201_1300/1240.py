from collections import deque


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        queue = deque((((n,) * m, 1),))
        while queue:
            arr, count = queue.popleft()
            if all(n == len(arr) for n in arr):
                return count
            start, end = 0, len(arr)
            for i, n in enumerate(arr):
                if n > arr[start]:
                    start = i
                elif n < arr[start]:
                    end = i + 1
                    break
            for i in range(min(arr[start], end - start), 0, -1):
                next_arr = arr[:start] + tuple(n - i for n in arr[start:start + i]) + arr[start + i:]
                while next_arr[0] == 0:
                    next_arr = next_arr[1:]
                while next_arr[-1] == 0:
                    next_arr = next_arr[:-1]
                queue.append((next_arr, count + 1))
        return -1
