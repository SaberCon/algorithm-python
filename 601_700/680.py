def is_palindrome(s):
    return s == s[::-1]


class Solution:
    def validPalindrome(self, s: str) -> bool:
        end = len(s) - 1
        for i in range((end + 1) // 2):
            if s[i] == s[end - i]:
                continue
            return is_palindrome(s[i:end - i]) or is_palindrome(s[i + 1:end - i + 1])
        return True
