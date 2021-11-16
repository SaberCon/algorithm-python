class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=lambda n: (n < 0, abs(n)))
        seen = set()
        cur = 1
        for i, n in enumerate(arr):
            if i in seen:
                continue
            while cur < len(arr) and arr[cur] != 2 * n:
                cur += 1
            if cur == len(arr):
                return False
            seen.add(cur)
            cur += 1
        return True
