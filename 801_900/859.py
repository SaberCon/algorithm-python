class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        mismatch = []
        for a, b in zip(s, goal):
            if a == b:
                continue
            if len(mismatch) > 1:
                return False
            mismatch.append(a + b)
        if mismatch:
            return len(mismatch) > 1 and mismatch[0] == mismatch[1][::-1]
        return len(set(s)) < len(s)
