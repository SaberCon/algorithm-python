class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join((w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * (i + 1)
                        for i, w in enumerate(S.split()))
