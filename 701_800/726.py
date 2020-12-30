class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = {}
        
        return ''.join(name + (str(count) if count > 1 else '') for name, count in sorted(counts.items()))
