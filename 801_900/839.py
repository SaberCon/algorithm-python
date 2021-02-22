class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(str1, str2):
            diff = 0
            for c1, c2 in zip(str1, str2):
                if c1 != c2:
                    if diff >= 2:
                        return False
                    diff += 1
            return True

        similarities = [[] for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for j in range(i + 1, len(strs)):
                if is_similar(s, strs[j]):
                    similarities[i].append(j)
                    similarities[j].append(i)
        seen = set()
        ans = 0

        def dfs(i):
            seen.add(i)
            for si in similarities[i]:
                if si not in seen:
                    dfs(si)

        for i in range(len(strs)):
            if i in seen:
                continue
            ans += 1
            dfs(i)
        return ans
