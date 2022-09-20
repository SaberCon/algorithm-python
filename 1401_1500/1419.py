class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        frogs = [0] * 5
        for i in ('croak'.index(c) for c in croakOfFrogs):
            if i == 0:
                frogs[0] += 1
                ans = max(ans, sum(frogs))
                continue
            if frogs[i - 1] < 1:
                return -1
            frogs[i - 1] -= 1
            if i < 4:
                frogs[i] += 1
        return ans if all(f == 0 for f in frogs) else -1
