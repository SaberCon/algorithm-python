class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        mi, ma = 0, len(s)
        for c in s:
            if c == 'I':
                ans.append(mi)
                mi += 1
            else:
                ans.append(ma)
                ma -= 1
        ans.append(mi)
        return ans
