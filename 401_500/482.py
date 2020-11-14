class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        start = len(S) % K
        ans = S[0:start]
        while start < len(S):
            ans += '-' + S[start:start + K]
            start += K
        return ans[1:] if ans.startswith('-') else ans
