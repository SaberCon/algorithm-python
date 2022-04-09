class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def to_arr(cs):
            ans = [0] * 26
            for c in cs:
                ans[ord(c) - ord('a')] += 1
            return ans

        chars = to_arr(chars)
        return sum(len(w) for w in words if all(a <= b for a, b in zip(to_arr(w), chars)))
