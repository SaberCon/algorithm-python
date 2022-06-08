from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def palindrome(left: int, right: int) -> int:
            if left >= right:
                return 0
            return (s[left] != s[right]) + palindrome(left + 1, right - 1)

        @cache
        def partition(size: int, num: int) -> int:
            if num == 1:
                return palindrome(0, size - 1)
            return min(palindrome(i, size - 1) + partition(i, num - 1) for i in range(num - 1, size))

        return partition(len(s), k)
