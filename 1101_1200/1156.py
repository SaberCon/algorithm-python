class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counts = [0] * 26
        letters = []
        for c in text:
            i = ord(c) - ord('a')
            counts[i] += 1
            if letters and letters[-1][0] == i:
                letters[-1][1] += 1
            else:
                letters.append([i, 1])
        ans = 0
        for j, (i, s) in enumerate(letters):
            if j > 1 and letters[j - 1][1] == 1 and letters[j - 2][0] == i:
                s += letters[j - 2][1]
            ans = max(ans, min(counts[i], s + 1))
        return ans
