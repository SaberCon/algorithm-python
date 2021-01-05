from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        return letters[bisect_right(letters, target)]
