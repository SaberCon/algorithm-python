import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = [(-1, 0)]
        for n in arr1:
            top_operations = {}
            for top, operations in dp:
                i = bisect.bisect_right(arr2, top)
                if i < len(arr2):
                    top_operations[arr2[i]] = operations + 1
                if top < n:
                    top_operations[n] = operations
            dp = []
            for top in sorted(top_operations.keys()):
                operations = top_operations[top]
                if dp and dp[-1][1] <= operations:
                    continue
                dp.append((top, operations))
            if not dp:
                return -1
        return dp[-1][1]
