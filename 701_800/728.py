class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if all(c != '0' and i % int(c) == 0 for c in str(i))]
