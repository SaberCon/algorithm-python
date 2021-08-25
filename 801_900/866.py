class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            return num > 1 and all(num % i for i in range(2, int(num ** 0.5) + 1))

        def get_next_palindrome(num):
            chars = str(num)
            size = len(chars)
            half = chars[:(size + 1) // 2]
            palindrome = int(half + half[(-1 - size % 2)::-1])
            if palindrome > num:
                return palindrome
            next_half = str(int(half) + 1)
            return int(next_half + next_half[(-1 - size % 2 - len(next_half) + len(half))::-1])

        n = n - 1
        while True:
            n = get_next_palindrome(n)
            if is_prime(n):
                return n
