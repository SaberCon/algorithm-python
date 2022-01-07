class Solution:
    def clumsy(self, n: int) -> int:
        def calc(num):
            if num < 3:
                return -num
            return -(num * (num - 1) // (num - 2)) + num - 3

        return 2 * (n * (n - 1) // (n - 2)) + sum(calc(i) for i in range(n, 0, -4)) if n >= 3 else n
