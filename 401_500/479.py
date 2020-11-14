class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        _max = 10 ** n - 1
        for i in range(_max, 0, -1):
            palindrome = int(str(i) + str(i)[::-1])
            for j in range(_max, int(palindrome ** 0.5) - 1, -1):
                if palindrome % j == 0 and palindrome // j < _max:
                    return palindrome % 1337
        return -1
