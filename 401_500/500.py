class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [set('qwertyuiopQWERTYUIOP'), set('asdfghjklASDFGHJKL'), set('zxcvbnmZXCVBNM')]
        return [word for word in words if any(line.issuperset(set(word)) for line in lines)]
