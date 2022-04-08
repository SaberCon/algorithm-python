from collections import Counter


class MajorityChecker:

    def __init__(self, arr: List[int]):
        N = len(arr)
        s = max(10, int((N * 2) ** 0.5))
        nums = {k: [0] * (N + 1) for k, v in Counter(arr).items() if v > s // 2}
        for i in range(N):
            for k in nums.keys():
                nums[k][i] = nums[k][i - 1]
            if arr[i] in nums:
                nums[arr[i]][i] += 1
        self.s = s
        self.arr = arr
        self.nums = nums

    def query(self, left: int, right: int, threshold: int) -> int:
        if right - left + 1 <= self.s:
            return self.query1(left, right, threshold)
        else:
            return self.query2(left, right, threshold)

    def query1(self, left: int, right: int, threshold: int) -> int:
        n = k = 0
        for i in range(left, right + 1):
            if n == self.arr[i]:
                k += 1
            elif k > 0:
                k -= 1
            else:
                n = self.arr[i]
        return n if sum(self.arr[i] == n for i in range(left, right + 1)) >= threshold else -1

    def query2(self, left: int, right: int, threshold: int) -> int:
        for k in self.nums.keys():
            if self.nums[k][right] - self.nums[k][left - 1] >= threshold:
                return k
        return -1
