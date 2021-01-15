from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((count - count % (num + 1) + num + 1 if count % (num + 1) else count) for num, count in
                   Counter(answers).items())
