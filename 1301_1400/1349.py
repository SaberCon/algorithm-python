from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        schemes = [(i, bin(i).count('1')) for i in range(1 << len(seats[0])) if i & (i << 1) == 0]
        dp = [(0, 0)]
        for row in seats:
            row = sum(1 << i for i, s in enumerate(row) if s == '.')
            dp = [(scheme, count + max(c for i, c in dp if i & ((scheme << 1) | (scheme >> 1)) == 0))
                  for scheme, count in schemes if scheme | row == row]
        return max(c for _, c in dp)
