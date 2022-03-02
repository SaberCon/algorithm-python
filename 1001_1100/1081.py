class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ans = []
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in s:
            if c not in ans:
                while ans and ans[-1] > c and count[ord(ans[-1]) - ord('a')] > 0:
                    ans.pop()
                ans.append(c)
            count[ord(c) - ord('a')] -= 1
        return ''.join(ans)
