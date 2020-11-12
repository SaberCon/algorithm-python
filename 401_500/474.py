class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [(s.count('0'), s.count('1')) for s in strs]

