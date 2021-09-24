class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set()
        for n in arr:
            cur = {i | n for i in cur} | {n}
            ans.update(cur)
        return len(ans)
