from bisect import bisect_right


class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snapshot = 0

    def set(self, index: int, val: int) -> None:
        arr = self.arr[index]
        if arr[-1][0] == self.snapshot:
            arr.pop()
        arr.append((self.snapshot, val))

    def snap(self) -> int:
        self.snapshot += 1
        return self.snapshot - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        i = bisect_right(arr, (snap_id, 10 ** 9 + 1))
        return arr[i - 1][1]
