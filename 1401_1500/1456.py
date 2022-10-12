class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = sum(s[i] in 'aeiou' for i in range(k))
        ans = count
        for i in range(k, len(s)):
            count += (s[i] in 'aeiou') - (s[i - k] in 'aeiou')
            ans = max(ans, count)
        return ans
