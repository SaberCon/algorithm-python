class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        size = 0
        for c in s:
            curr = widths[ord(c) - ord('a')]
            if curr + size > 100:
                lines += 1
                size = curr
            else:
                size += curr
        return [lines, size]
