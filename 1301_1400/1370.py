class Solution:
    def sortString(self, s: str) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        ans = []
        for i in range(max(count)):
            chars = ''.join(chr(j + ord('a')) for j, c in enumerate(count) if c > i)
            ans.append(chars if i % 2 == 0 else chars[::-1])
        return ''.join(ans)
