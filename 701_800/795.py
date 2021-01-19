class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        def count_less(top):
            ans = size = 0
            for num in A:
                if num > top:
                    size = 0
                    continue
                size += 1
                ans += size
            return ans

        return count_less(R) - count_less(L - 1)
