class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        size = len(start)
        i = j = 0
        while True:
            while i < size and start[i] == 'X':
                i += 1
            while j < size and end[j] == 'X':
                j += 1
            if i == size or j == size:
                return i == size and j == size
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
