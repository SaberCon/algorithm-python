from functools import cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def distance(letter1: str, letter2: str) -> int:
            i1, i2 = ord(letter1) - ord('A'), ord(letter2) - ord('A')
            x1, y1, x2, y2 = i1 // 6, i1 % 6, i2 // 6, i2 % 6
            return abs(x1 - x2) + abs(y1 - y2)

        @cache
        def min_distance(finger1: int, finger2: int) -> int:
            if (finger1 == - 1 and finger2 == 0) or (finger1 == 0 and finger2 == 1):
                return 0
            if finger2 > finger1 + 1:
                return min_distance(finger1, finger2 - 1) + distance(word[finger2 - 1], word[finger2])
            return min(min(min_distance(i, finger1) + distance(word[i], word[finger2]) for i in range(finger1)),
                       min_distance(-1, finger1))

        return min(min_distance(i, len(word) - 1) for i in range(len(word) - 1))
