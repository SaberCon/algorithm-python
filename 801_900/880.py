class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        size = 0
        for c in s:
            stack.append(c)
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
            if size >= k:
                break
        while stack:
            c = stack.pop()
            if c.isdigit():
                size //= int(c)
                k = k % size if k % size else size
            elif size == k:
                return c
            else:
                size -= 1
