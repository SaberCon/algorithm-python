class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return ['']
        return [c + s for c in [*{S[0].lower(), S[0].upper()}] for s in self.letterCasePermutation(S[1:])]
