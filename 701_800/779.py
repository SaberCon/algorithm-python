class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1:
            return 0
        if K > 2 ** (N - 2):
            return 0 if self.kthGrammar(N - 1, K - 2 ** (N - 2)) else 1
        else:
            return self.kthGrammar(N - 1, K)