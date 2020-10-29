class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needs = {}
        for c in p:
            needs[c] = needs.get(c, 0) + 1
        ans = []
        window = {}
        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1
            start = i - len(p)
            if start >= 0:
                window[s[start]] -= 1
                if not window[s[start]]:
                    del window[s[start]]
            if window == needs:
                ans.append(start + 1)
        return ans
