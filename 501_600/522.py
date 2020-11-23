class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub(s1, s2):
            if not s1:
                return True
            index = 0
            for s in s2:
                if s == s1[index]:
                    index += 1
                if index >= len(s1):
                    return True
            return False

        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            sub = False
            for j in range(len(strs)):
                if len(strs[j]) < len(strs[i]):
                    break
                if i != j and is_sub(strs[i], strs[j]):
                    sub = True
                    break
            if not sub:
                return len(strs[i])
        return -1
