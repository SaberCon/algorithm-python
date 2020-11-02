class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def find_kth_number(prefix, k):
            if k == 1:
                return prefix
            curr = prefix
            next = curr + 1
            count = 0
            while curr <= n:
                count += min(next, n + 1) - curr
                curr *= 10
                next *= 10
            return find_kth_number(prefix + 1, k - count) if count < k else find_kth_number(prefix * 10, k - 1)

        return find_kth_number(1, k)
