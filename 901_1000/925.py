class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        typed += 'E'
        name += 'E'
        index = 0
        for c in name:
            while index > 0 and typed[index] == typed[index - 1] and typed[index] != c:
                index += 1
            if typed[index] != c:
                return False
            index += 1
        return True
