class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        left_size, left_index = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                left_size += 1
            else:
                left_size -= 1
            if left_size == 0:
                ans.append(s[left_index + 1:i])
                left_index = i + 1
        return ''.join(ans)
